--SELECT STATEMENTs

SELECT 
    i.Name AS ItemName,
    i.Description AS ItemDescription,
    m.Description AS MaterialDescription,
    c.Description AS ColourDescription
FROM 
    Item i
JOIN 
    ItemColour ic ON i.ItemID = ic.ItemID
JOIN 
    ItemMaterial im ON i.ItemID = im.ItemID
JOIN 
    Material m ON im.MaterialID = m.MaterialID
JOIN 
    Colour c ON ic.ColourID = c.ColourID
WHERE 
    ic.ColourID = 4;



SELECT
    -- Grouping fields
    it.Name AS ItemName,
    it.Description AS ItemDescription,
    m.Description AS MaterialDescription,
    c.Description AS ColourDescription,
    ad.AddressLine1 AS DepotAddressLine1,
    ad.Postcode AS DepotPostCode,
    -- Aggregate function for the field
    SUM(oi.Quantity) AS TotalOrderedQuantity
FROM 
    `Order` o
    -- Join together all related tables that store the data to display.
JOIN 
    OrderItem oi ON o.OrderNumber = oi.OrderNumber
JOIN 
    Item it ON oi.ItemID = it.ItemID
JOIN 
    ItemMaterial im ON oi.ItemMaterialID = im.ItemMaterialID
JOIN 
    Material m ON im.MaterialID = m.MaterialID
JOIN 
    ItemColour ic ON oi.ItemColourID = ic.ItemColourID
JOIN 
    Colour c ON ic.ColourID = c.ColourID
JOIN 
    DepotItem di ON oi.DepotItemID = di.DepotItemID
JOIN 
    Depot d ON di.DepotID = d.DepotID
JOIN 
    Address ad ON d.AddressID = ad.AddressID
-- Grouping clause to combine matching combinations of Item, Colour and Material
GROUP BY 
    it.Name,
    it.Description,
    m.Description,
    c.Description,
    ad.AddressLine1,
    ad.Postcode
ORDER BY 
    -- Show the best sellers first.
    ad.AddressLine1 DESC,
    TotalOrderedQuantity DESC;



-- Find orders that have gone over a companies credit limit.
SELECT
    o.OrderNumber,
    o.Status,
    c.CompanyID,
    c.CreditLimit,
    SUM(i.price * oi.Quantity) AS TotalOrderPrice
FROM `Order` o
JOIN OrderItem oi ON o.OrderNumber = oi.OrderNumber
JOIN Item i ON oi.ItemID = i.ItemID
JOIN Company c ON o.CompanyID = c.CompanyID
GROUP BY o.OrderNumber, c.CompanyID, c.CreditLimit
HAVING TotalOrderPrice > c.CreditLimit;

-- Extends the query from above.
-- Create a temporary table to store the OrderNumbers
CREATE TEMPORARY TABLE TempOrdersToCancel (OrderNumber integer unsigned);

-- Insert the OrderNumbers of orders that exceed the credit limit into the temporary table
INSERT INTO TempOrdersToCancel
SELECT
    o.OrderNumber
FROM `Order` o
JOIN OrderItem oi ON o.OrderNumber = oi.OrderNumber
JOIN Item i ON oi.ItemID = i.ItemID
JOIN Company c ON o.CompanyID = c.CompanyID
GROUP BY o.OrderNumber, c.CompanyID, c.CreditLimit
HAVING SUM(i.price * oi.Quantity) > c.CreditLimit;

-- Update the orders based on the OrderNumbers in the temporary table
UPDATE `Order`
SET Status = 'CANCELLED'
WHERE OrderNumber IN (SELECT OrderNumber FROM TempOrdersToCancel);

-- Return the cancelled orders
SELECT * FROM `Order` WHERE OrderNumber IN (SELECT OrderNumber FROM TempOrdersToCancel);



DELIMITER //
-- Create a new Stored Procedure that can be re-used.
CREATE PROCEDURE UpdateStockForFirstTwoDepotItems()
BEGIN
    -- Initialize counter
    DECLARE counter INT DEFAULT 0;
    DECLARE depot_count INT DEFAULT 0;
    DECLARE current_depot INT;
    DECLARE first_item INT;
    DECLARE second_item INT;

    -- Fetch total number of depots
    SELECT COUNT(*) INTO depot_count FROM `Depot`;

    -- Iterate over each depot
    WHILE counter < depot_count DO
        -- Fetch DepotID at current counter position
        SELECT `DepotID` INTO current_depot FROM `Depot` LIMIT 1 OFFSET counter;

        -- Fetch the first DepotItem for the current depot
        SELECT `ItemID` INTO first_item 
        FROM `DepotItem` 
        WHERE `DepotID` = current_depot 
        LIMIT 1;

        -- Add 50 stock to the first DepotItem
        UPDATE `DepotItem` 
        SET `StockAmount` = `StockAmount` + 50 
        WHERE `DepotID` = current_depot AND `ItemID` = first_item;

        -- Fetch the second DepotItem for the current depot (assuming there's a second item)
        SELECT `ItemID` INTO second_item
        FROM `DepotItem` 
        WHERE `DepotID` = current_depot AND `ItemID` != first_item 
        LIMIT 1;

        -- Add 50 stock to the second DepotItem (if it exists)
        IF second_item IS NOT NULL THEN
            UPDATE `DepotItem` 
            SET `StockAmount` = `StockAmount` + 50 
            WHERE `DepotID` = current_depot AND `ItemID` = second_item;
        END IF;

        -- Increment counter
        SET counter = counter + 1;
    END WHILE;
END //
DELIMITER ;


-- Invoke the Stored Procedure
CALL UpdateStockForFirstTwoDepotItems(); 


-- Display all Employees.
SELECT 
    e.EmployeeID,
    p.FirstName,
    p.LastName,
    p.ContactNumber,
    p.EmailAddress,
    e.IsAdministrator
FROM 
    Employee e
JOIN 
    Person p ON e.PersonID = p.PersonID
ORDER BY 
    e.EmployeeID;





DELIMITER //
-- Handles creation of database server accounts with appropriate grants.
CREATE PROCEDURE CreateUserForEmployees()
BEGIN
    -- Define variables for use programmatically.
    DECLARE done INT DEFAULT 0;
    DECLARE user_name VARCHAR(255);
    DECLARE is_admin BOOLEAN;
    
    -- Declare cursor for employee-person joined rows
    DECLARE employee_cursor CURSOR FOR 
    SELECT CONCAT(p.FirstName, '_', p.LastName), e.IsAdministrator 
    FROM Employee e 
    JOIN Person p ON e.PersonID = p.PersonID;
    
    -- Declare handler for end of loop
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN employee_cursor;

    emp_loop: LOOP
        FETCH employee_cursor INTO user_name, is_admin;
        IF done THEN
            LEAVE emp_loop;
        END IF;

        -- Create the user script
        SET @create_user_query = CONCAT('CREATE USER \'', user_name, '\'@\'localhost\' IDENTIFIED BY \'defaultPassword123\';');
        PREPARE stmt FROM @create_user_query;

        -- Execute the user script.
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Create a script to grant privileges based on the IsAdministrator flag
        IF is_admin THEN
            SET @grant_query = CONCAT('GRANT ALL PRIVILEGES ON *.* TO \'', user_name, '\'@\'localhost\';');
        ELSE
            -- Here, grant limited permissions.
            SET @grant_query = CONCAT('GRANT SELECT ON joshdb.* TO \'', user_name, '\'@\'localhost\';');
        END IF;
  
        PREPARE stmt FROM @grant_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP emp_loop;

    CLOSE employee_cursor;
END //

DELIMITER ;

-- Invoke the Stored Procedure
CALL CreateUserForEmployees(); 

DELIMITER //
CREATE PROCEDURE CreateCompanyWithItems(
    IN item1 INT, 
    IN item2 INT, 
    IN item3 INT, 
    IN item4 INT
)
BEGIN

    -- Create a company
    INSERT INTO `Company` (AccountNumber, CreditLimit) VALUES ('ACC0067890', 50000.00);

    -- Store the ID of the last inserted company for later use
    SET @last_company_id = LAST_INSERT_ID();

    -- Create two users (customers) linked to this company
    -- For this, we'll need to first create two "Persons" and then link them to the customer table

    -- User 1
    INSERT INTO `Person` (FirstName, LastName, ContactNumber, EmailAddress) VALUES ('James', 'Matherson', '0123456789', 'james.matherson@example.com');
    INSERT INTO `Customer` (CompanyID, PersonID) VALUES (@last_company_id, LAST_INSERT_ID());

    -- User 2
    INSERT INTO `Person` (FirstName, LastName, ContactNumber, EmailAddress) VALUES ('Jade', 'Beckford', '9876543210', 'jade.beckford@example.com');
    INSERT INTO `Customer` (CompanyID, PersonID) VALUES (@last_company_id, LAST_INSERT_ID());

    -- Allow the specified items for the company
    INSERT INTO `CompanyAllowedItem` (CompanyID, ItemID) VALUES (@last_company_id, item1), (@last_company_id, item2), (@last_company_id, item3), (@last_company_id, item4);

END //
DELIMITER ;

-- Invoke the Stored Procedure
CALL CreateCompanyWithItems(1, 2, 3, 4); 


SELECT 
    i.ItemID,
    i.Name,
    i.Description,
    i.price
FROM 
    `CompanyAllowedItem` AS cai
INNER JOIN 
    `Item` AS i ON cai.ItemID = i.ItemID
WHERE 
    cai.CompanyID = (
        SELECT 
            CompanyID 
        FROM 
            Company 
        ORDER BY 
            CompanyID DESC 
        LIMIT 1
    );




-- Insert a new order for Company 5
INSERT INTO `Order` (CompanyID, Status) VALUES (5, 'PLACED');

-- Store the last inserted order number into a variable
SET @latestOrderNumber = LAST_INSERT_ID();

-- Fetch the first two ItemIDs from the CompanyAllowedItems table for Company 5
SET @firstItemID = (SELECT `ItemID` FROM `CompanyAllowedItem` WHERE `CompanyID` = 5 ORDER BY `ItemID` LIMIT 1);
SET @secondItemID = (SELECT `ItemID` FROM `CompanyAllowedItem` WHERE `CompanyID` = 5 AND `ItemID` != @firstItemID ORDER BY `ItemID` LIMIT 1);

-- Insert the first OrderItem from the first occurrence of the first ItemID in the DepotItem table
INSERT INTO `OrderItem` (Quantity, ItemID, DepotItemID, ItemMaterialID, ItemColourID, OrderNumber)
SELECT
    1 AS Quantity,
    di.ItemID,
    di.DepotItemId,
    im.ItemMaterialID,
    ic.ItemColourID,
    @latestOrderNumber AS OrderNumber
FROM `DepotItem` di
JOIN `ItemMaterial` im ON di.ItemID = im.ItemID
JOIN `ItemColour` ic ON di.ItemID = ic.ItemID
WHERE di.ItemID = @firstItemID
LIMIT 1;

-- Insert the first OrderItem from the first occurrence of the second ItemID in the DepotItem table
INSERT INTO `OrderItem` (Quantity, ItemID, DepotItemID, ItemMaterialID, ItemColourID, OrderNumber)
SELECT
    1 AS Quantity,
    di.ItemID,
    di.DepotItemId,
    im.ItemMaterialID,
    ic.ItemColourID,
    @latestOrderNumber AS OrderNumber
FROM `DepotItem` di
JOIN `ItemMaterial` im ON di.ItemID = im.ItemID
JOIN `ItemColour` ic ON di.ItemID = ic.ItemID
WHERE di.ItemID = @secondItemID
LIMIT 1;




-- Fetch details of the entire order for the latest order number

SELECT 
    o.OrderNumber,
    o.Status,
    o.OrderDate,
    o.DeliveryDate,
    c.CompanyID,
    c.AccountNumber,
    oi.Quantity,
    i.Name AS ItemName,
    i.Description AS ItemDescription,
    m.Description AS MaterialDescription,
    col.Description AS ColourDescription,
    di.StockAmount,
    d.AddressID AS DepotAddress,
    oi.Quantity * i.price AS OrderItemPrice
FROM `Order` o
JOIN Company c ON o.CompanyID = c.CompanyID
JOIN OrderItem oi ON o.OrderNumber = oi.OrderNumber
JOIN Item i ON oi.ItemID = i.ItemID
JOIN ItemMaterial im ON oi.ItemMaterialID = im.ItemMaterialID
JOIN Material m ON im.MaterialID = m.MaterialID
JOIN ItemColour ic ON oi.ItemColourID = ic.ItemColourID
JOIN Colour col ON ic.ColourID = col.ColourID
JOIN DepotItem di ON oi.DepotItemID = di.DepotItemId
JOIN Depot d ON di.DepotID = d.DepotID
WHERE o.OrderNumber = @latestOrderNumber;




 SELECT 
     SUM(oi.Quantity * i.price) AS TotalOrderPrice
 FROM OrderItem oi
 JOIN Item i ON oi.ItemID = i.ItemID
 WHERE oi.OrderNumber = @latestOrderNumber;