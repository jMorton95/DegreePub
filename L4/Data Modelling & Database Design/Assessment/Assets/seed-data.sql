-- Seed Some Pre-defined Colours
INSERT INTO `Colour` (`Description`)
VALUES 
('Gold'),
('Silver'),
('Rose Gold'),
('Emerald Green'),
('Ruby Red'),
('Sapphire Blue'),
('Diamond Clear'),
('Amethyst Purple'),
('Onyx Black'),
('Pearl White');

-- Seed Some Pre-defined Materials.
INSERT INTO `Material` (`Description`)
VALUES 
('Gold 24K'),
('Gold 18K'),
('White Gold 18K'),
('Sterling Silver'),
('Platinum'),
('Titanium'),
('Copper'),
('Bronze'),
('Stainless Steel'),
('Diamond'),
('Emerald'),
('Ruby'),
('Sapphire'),
('Amethyst'),
('Onyx'),
('Pearl');

-- Seed 10 Addresses using a Fancy & Fake naming convention.
INSERT INTO `Address` (`AddressLine1`, `AddressLine2`, `AddressLine3`, `Town`, `County`, `Postcode`)
VALUES ('123 Jewel St', 'Diamond District', 'Riverside Plaza', 'Gemsville', 'Ruby County', 'WF1 3ST'),
       ('456 Crystal Ave', 'Emerald Enclave', 'Peachtree Heights', 'Gemsville', 'Ruby County', 'JW5 5LC'),
       ('789 Platinum Pl', 'Silver Shore', 'Elmwood Estates', 'Stoneville', 'Pearl Parish', 'ST7 1DC'),
       ('101 Gold Ln', 'Golden Gate', 'Oakwood Gardens', 'Stoneville', 'Pearl Parish', 'OG1 8FC'),
       ('202 Sapphire Sq', 'Ruby Region', 'Sunflower Suites', 'Crystal City', 'Sapphire State', 'CC1 4FH'),
       ('303 Amethyst Alcove', 'Pearl Park', 'Cedarview Terrace', 'Crystal City', 'Sapphire State', 'CC4 6XS'),
       ('404 Diamond Dr', 'Platinum Point', 'Pine Hill Lane', 'Jewel Junction', 'Topaz Territory', 'JJ4 9JG'),
       ('505 Emerald Esplanade', 'Copper Corner', 'Ivybridge Court', 'Jewel Junction', 'Topaz Territory', 'JJ6 7HT'),
       ('606 Ruby Rd', 'Sapphire Street', 'Maple Meadows', 'Gem Grove', 'Emerald Empire', 'GG6 5MR'),
       ('707 Topaz Tr', 'Amethyst Avenue', 'Birchwood Square', 'Gem Grove', 'Emerald Empire', 'GG7 2XL');

-- Seed our 2 Depos with the first 2 addresses.
INSERT INTO `Depot` (`AddressID`)
VALUES (1), (2);

-- Seed 20 aptly named items.
INSERT INTO `Item` (`Name`, `Description`, `price`)
VALUES 
('Golden Ring', 'Elegant golden ring.', 250.00),
('Silver Necklace', 'Beautiful silver necklace.', 150.00),
('Platinum Bracelet', 'Stylish platinum bracelet.', 400.00),
('Diamond Earrings', 'Sparkling diamond earrings.', 550.00),
('Emerald Brooch', 'Vintage emerald brooch.', 320.00),
('Ruby Locket', 'Stunning ruby locket.', 350.00),
('Sapphire Pendant', 'Dazzling sapphire pendant.', 270.00),
('Amethyst Choker', 'Charming amethyst choker.', 210.00),
('Pearl Necklace', 'Classic pearl necklace.', 200.00),
('Golden Studs', 'Shiny golden earrings.', 120.00),
('Silver Anklet', 'Dainty silver anklet.', 80.00),
('Platinum Nose Ring', 'Unique platinum nose ring.', 90.00),
('Diamond Tiara', 'Royal diamond tiara.', 650.00),
('Emerald Cufflinks', 'Exquisite emerald cufflinks.', 180.00),
('Ruby Crown', 'Magnificent ruby crown.', 590.00),
('Sapphire Ring', 'Elegant sapphire ring.', 280.00),
('Amethyst Bracelet', 'Alluring amethyst bracelet.', 210.00),
('Pearl Studs', 'Sophisticated pearl earrings.', 100.00),
('Golden Toe Ring', 'Trendy golden toe ring.', 60.00),
('Silver Brooch', 'Elegant silver brooch.', 110.00);


-- For each item, assign 3 Materials.
INSERT INTO `ItemMaterial` (`ItemID`, `MaterialID`) VALUES 
(1, 1), (1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (3, 5), (3, 6), (3, 9), 
(4, 10), (4, 4), (4, 5), (5, 11), (5, 4), (5, 3), (6, 12), (6, 1), (6, 2), 
(7, 13), (7, 4), (7, 5), (8, 14), (8, 4), (8, 6), (9, 16), (9, 1), (9, 3), 
(10, 1), (10, 2), (10, 3), (11, 4), (11, 7), (11, 8), (12, 5), (12, 6), (12, 9), 
(13, 10), (13, 1), (13, 3), (14, 11), (14, 1), (14, 4), (15, 12), (15, 1), (15, 3), 
(16, 13), (16, 4), (16, 1), (17, 14), (17, 4), (17, 6), (18, 16), (18, 1), (18, 3), 
(19, 1), (19, 2), (19, 3), (20, 4), (20, 5), (20, 6);

-- For each item, assign 3 Colours
INSERT INTO `ItemColour` (`ItemID`, `ColourID`)
VALUES (1, 1), (1, 2), (1, 3), (2, 2), (2, 4), (2, 5), (3, 3), (3, 4), (3, 6), 
(4, 7), (4, 8), (4, 9), (5, 4), (5, 5), (5, 10), (6, 5), (6, 6), (6, 7), 
(7, 6), (7, 7), (7, 8), (8, 8), (8, 9), (8, 10), (9, 1), (9, 3), (9, 4), 
(10, 2), (10, 3), (10, 10), (11, 3), (11, 6), (11, 7), (12, 4), (12, 7), (12, 8), 
(13, 5), (13, 8), (13, 9), (14, 6), (14, 9), (14, 10), (15, 7), (15, 10), (15, 2), 
(16, 8), (16, 1), (16, 3), (17, 9), (17, 3), (17, 5), (18, 10), (18, 4), (18, 6), 
(19, 1), (19, 7), (19, 8), (20, 2), (20, 9), (20, 10);

-- For each Depot, Assign 10 items with a StockAmount of 100.
INSERT INTO `DepotItem` (`DepotID`, `ItemID`, `StockAmount`) VALUES
(1, 1, 100), (1, 2, 100), (1, 3, 100), (1, 4, 100), (1, 5, 100), (1, 6, 100),
(1, 7, 100), (1, 8, 100), (1, 9, 100), (1, 10, 100), 
(2, 11, 100), (2, 12, 100), (2, 13, 100), (2, 14, 100), (2, 15, 100), 
(2, 16, 100), (2, 17, 100), (2, 18, 100), (2, 19, 100), (2, 20, 100);

-- Seed 4 Companies, one with a Credit Limit.
INSERT INTO `Company` (`AccountNumber`, `CreditLimit`, `InvoiceAddress`, `DeliveryAddress`)
VALUES ('ACC00123456', NULL, 3, 4), ('ACC00123457', 10000, 5, 6),
('ACC00123458', NULL, 7, 8), ('ACC00123459', NULL, 9, 10);

-- Seed 10 pseudo-random people.
INSERT INTO `Person` (`FirstName`, `LastName`, `ContactNumber`, `EmailAddress`)
VALUES 
('John', 'Doe', '+44 7700 900001', 'john.doe@email.com'),
('Jane', 'Smith', '+44 7700 900002', 'jane.smith@email.com'),
('Emily', 'Johnson', '+44 7700 900003', 'emily.johnson@email.com'),
('Michael', 'Brown', '+44 7700 900004', 'michael.brown@email.com'),
('Sophia', 'Taylor', '+44 7700 900005', 'sophia.taylor@email.com'),
('William', 'Jones', '+44 7700 900006', 'william.jones@email.com'),
('Olivia', 'White', '+44 7700 900007', 'olivia.white@email.com'),
('James', 'Harris', '+44 7700 900008', 'james.harris@email.com'),
('Isabella', 'Clark', '+44 7700 900009', 'isabella.clark@email.com'),
('Benjamin', 'Walker', '+44 7700 900010', 'benjamin.walker@email.com');

-- Seed 2 Employees, one Admin.
INSERT INTO `Employee` (`IsAdministrator`, `PersonID`)
VALUES (1, 1), (0, 2);

-- For each of our companies, assign 2 of our people as Customers, one with ordering privileges.
INSERT INTO `Customer` (`CanCreateOrder`, `CompanyID`, `PersonID`)
VALUES (1, 1, 3), (0, 1, 4), (1, 2, 5), (0, 2, 6),
(1, 3, 7), (0, 3, 8), (1, 4, 9), (0, 4, 10);

-- For each company, seed 10 items that they're approved to purchase.
INSERT INTO `CompanyAllowedItem` (`CompanyID`, `ItemID`)
VALUES 
(1, 1), (1, 3), (1, 5), (1, 7), (1, 9), (1, 11), (1, 13), (1, 15), (1, 17), (1, 19),
(2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (2, 12), (2, 14), (2, 16), (2, 18), (2, 20),
(3, 1), (3, 2), (3, 4), (3, 6), (3, 7), (3, 9), (3, 11), (3, 13), (3, 15), (3, 17),
(4, 3), (4, 5), (4, 8), (4, 10), (4, 12), (4, 14), (4, 16), (4, 18), (4, 19), (4, 20);

-- Seed 3 orders for each Company. Order 3 for Company 2 will be special, as it will be cancelled because of going over the credit limit.
INSERT INTO `Order` (`Status`, `OrderDate`, `DeliveryDate`, `CompanyID`)
VALUES 
('PLACED', '2023-08-10 10:30:00', NULL, 1),
('SHIPPED', '2023-08-05 11:45:00', '2023-08-12 11:45:00', 1),
('COMPLETED', '2023-07-25 12:15:00', '2023-07-30 14:30:00', 1),

('PLACED', '2023-08-08 09:20:00', NULL, 2),
('SHIPPED', '2023-08-04 15:50:00', '2023-08-11 16:00:00', 2),
('PLACED', '2023-07-27 10:10:00', NULL, 2),

('PLACED', '2023-08-09 14:40:00', NULL, 3),
('SHIPPED', '2023-08-03 13:30:00', '2023-08-10 13:45:00', 3),
('COMPLETED', '2023-07-28 15:25:00', '2023-08-02 16:40:00', 3),

('PLACED', '2023-08-07 12:55:00', NULL, 4),
('SHIPPED', '2023-08-02 14:05:00', '2023-08-09 15:15:00', 4),
('COMPLETED', '2023-07-29 10:55:00', '2023-08-03 12:10:00', 4);


-- Seed 3 OrderItems per Order we just created.
INSERT INTO `OrderItem` (`Quantity`, `ItemID`, `DepotItemID`, `ItemMaterialID`, `ItemColourID`, `OrderNumber`)
VALUES 
(1, 1, 1, 1, 1, 1), (2, 2, 2, 4, 2, 1), (3, 3, 3, 7, 3, 1),
(1, 4, 4, 10, 7, 2), (2, 5, 5, 13, 4, 2), (3, 6, 6, 16, 5, 2),
(1, 7, 7, 19, 6, 3), (2, 8, 8, 22, 8, 3), (3, 9, 9, 25, 1, 3),
(1, 10, 10, 28, 2, 4), (2, 11, 11, 31, 3, 4), (3, 12, 12, 34, 4, 4),
(1, 13, 13, 37, 5, 5), (2, 14, 14, 40, 6, 5), (3, 15, 15, 43, 7, 5),
(16, 16, 16, 46, 8, 6), (24, 17, 17, 49, 9, 6), (34, 18, 18, 52, 10, 6),
(1, 19, 19, 55, 1, 7), (2, 20, 20, 58, 2, 7), (3, 1, 1, 1, 3, 7),
(1, 2, 2, 4, 4, 8), (2, 3, 3, 7, 5, 8), (3, 4, 4, 10, 6, 8),
(1, 5, 5, 13, 7, 9), (2, 6, 6, 16, 8, 9), (3, 7, 7, 19, 9, 9),
(1, 8, 8, 22, 10, 10), (2, 9, 9, 25, 1, 10), (3, 10, 10, 28, 2, 10),
(1, 11, 11, 31, 3, 11), (2, 12, 12, 34, 4, 11), (3, 13, 13, 37, 5, 11),
(4, 14, 14, 40, 6, 12), (5, 15, 15, 43, 7, 12), (6, 16, 16, 46, 8, 12);


-- Deduct the Quantity of the Items we just OrderItems for.
UPDATE DepotItem AS di
-- Join our OrderItems with our DepotItems
JOIN (
    SELECT
        oi.DepotItemID,
        -- Calculate the total Quantity per Item.
        SUM(oi.Quantity) AS TotalQuantity
    FROM OrderItem oi
    GROUP BY oi.DepotItemID
    -- Sum the aggregate of each Unique Item found in OrderItem records
) AS aggregatedOrderItems ON di.DepotItemId = aggregatedOrderItems.DepotItemID
-- Subtract the aggregated quantities from the Depot stock.
SET di.StockAmount = di.StockAmount - aggregatedOrderItems.TotalQuantity
WHERE di.DepotItemId IS NOT NULL;