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
    o.OrderNumber,
    it.Name AS ItemName,
    it.Description AS ItemDescription,
    m.Description AS MaterialDescription,
    c.Description AS ColourDescription,
    ad.AddressLine1,
    ad.AddressLine2,
    ad.AddressLine3,
    ad.Town,
    ad.County,
    ad.Postcode
FROM 
    `Order` o
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
WHERE 
    o.CompanyID = 2
AND 
    o.OrderNumber = (SELECT MIN(OrderNumber) FROM `Order` WHERE CompanyID = 2)
ORDER BY 
    o.OrderNumber;




SELECT
    o.OrderNumber,
    c.CompanyID,
    c.CreditLimit,
    SUM(i.price * oi.Quantity) AS TotalOrderPrice
FROM `Order` o
JOIN OrderItem oi ON o.OrderNumber = oi.OrderNumber
JOIN Item i ON oi.ItemID = i.ItemID
JOIN Company c ON o.CompanyID = c.CompanyID
GROUP BY o.OrderNumber, c.CompanyID, c.CreditLimit
HAVING TotalOrderPrice > c.CreditLimit;