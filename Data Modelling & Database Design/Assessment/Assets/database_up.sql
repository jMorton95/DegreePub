CREATE TABLE `Colour` (
  `ColourID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Description` varchar(255)
);

CREATE TABLE `ItemColour` (
  `ItemColourID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `ItemID` integer unsigned NOT NULL,
  `ColourID` integer unsigned NOT NULL,
  UNIQUE (`ItemID`, `ColourID`)
);

CREATE TABLE `Item` (
  `ItemID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Name` varchar(100) NOT NULL,
  `Inactive` boolean NOT NULL default 0,
  `Description` varchar(255),
  `price` decimal(10, 2)
);

CREATE TABLE `Material` (
  `MaterialID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Description` varchar(255)
);

CREATE TABLE `ItemMaterial` (
  `ItemMaterialID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `ItemID` integer unsigned NOT NULL,
  `MaterialID` integer unsigned NOT NULL,
  UNIQUE (`ItemID`, `MaterialID`)
);

CREATE TABLE `Depot` (
  `DepotID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `AddressID` integer unsigned NOT NULL
);

CREATE TABLE `DepotItem` (
  `DepotItemId` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `StockAmount` integer DEFAULT 0,
  `ItemID` integer unsigned NOT NULL,
  `DepotID` integer unsigned NOT NULL,
  FOREIGN KEY (`AddressID`) REFERENCES `Address` (`AddressID`) ON DELETE CASCADE;
);

CREATE TABLE `OrderItem` (
  `OrderItemID` bigint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Quantity` integer unsigned NOT NULL DEFAULT 1,
  `ItemID` integer unsigned NOT NULL,
  `DepotItemID` integer unsigned NOT NULL,
  `ItemMaterialID` integer unsigned NOT NULL,
  `ItemColourID` integer unsigned NOT NULL,
  `OrderNumber` integer unsigned NOT NULL,
  INDEX (`ItemID`, `OrderNumber`)
);

CREATE TABLE `Order` (
  `OrderNumber` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Status` ENUM('PLACED', 'SHIPPED', 'COMPLETED', 'CANCELLED') NOT NULL DEFAULT 'PLACED',
  `OrderDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `DeliveryDate` datetime,
  `CompanyID` integer unsigned,
  INDEX (`CompanyID`)
);

CREATE TABLE `CompanyAllowedItem` (
  `CompanyAllowedItemID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `CompanyID` integer unsigned NOT NULL,
  `ItemID` integer unsigned NOT NULL
);

CREATE TABLE `Company` (
  `CompanyID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `AccountNumber` varchar(12) NOT NULL UNIQUE,
  `CreditLimit` decimal(10, 2) DEFAULT NULL,
  `InvoiceAddress` integer unsigned,
  `DeliveryAddress` integer unsigned,
  FOREIGN KEY (`InvoiceAddressID`) REFERENCES `Address` (`AddressID`) ON DELETE CASCADE,
  FOREIGN KEY (`DeliveryAddressID`) REFERENCES `Address` (`AddressID`) ON DELETE CASCADE
);

CREATE TABLE `Customer` (
  `CustomerID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `CanCreateOrder` boolean NOT NULL DEFAULT 1,
  `CompanyID` integer unsigned NOT NULL,
  `PersonID` integer unsigned NOT NULL
);

CREATE TABLE `Address` (
  `AddressID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `AddressLine1` varchar(100) NOT NULL,
  `AddressLine2` varchar(100),
  `AddressLine3` varchar(100),
  `Town` varchar(100),
  `County` varchar(30),
  `Postcode` varchar(30) NOT NULL
);

CREATE TABLE `Person` (
  `PersonID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `FirstName` varchar(100),
  `LastName` varchar(100),
  `ContactNumber` varchar(30) NOT NULL,
  `EmailAddress` varchar(100) UNIQUE NOT NULL
);

CREATE TABLE `Employee` (
  `EmployeeID` integer unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `IsAdministrator` boolean NOT NULL DEFAULT 0,
  `PersonID` integer unsigned NOT NULL
);

ALTER TABLE `Depot`
ADD FOREIGN KEY (`AddressID`) REFERENCES `Address` (`AddressID`)
ON DELETE CASCADE;

ALTER TABLE `Order`
ADD FOREIGN KEY (`CompanyID`) REFERENCES `Company` (`CompanyID`)
ON DELETE SET NULL;

ALTER TABLE `Customer`
ADD FOREIGN KEY (`PersonID`) REFERENCES `Person` (`PersonID`);

ALTER TABLE `Company`
ADD FOREIGN KEY (`InvoiceAddress`) REFERENCES `Address` (`AddressID`)
ON DELETE CASCADE;

ALTER TABLE `Company`
ADD FOREIGN KEY (`DeliveryAddress`) REFERENCES `Address` (`AddressID`)
ON DELETE CASCADE;

ALTER TABLE `Employee`
ADD FOREIGN KEY (`PersonID`) REFERENCES `Person` (`PersonID`)
ON DELETE CASCADE;

ALTER TABLE `Customer`
ADD FOREIGN KEY (`CompanyID`) REFERENCES `Company` (`CompanyID`)
ON DELETE CASCADE;

ALTER TABLE `CompanyAllowedItem`
ADD FOREIGN KEY (`CompanyID`) REFERENCES `Company` (`CompanyID`)
ON DELETE CASCADE;

ALTER TABLE `CompanyAllowedItem`
ADD FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`)
ON DELETE CASCADE;

ALTER TABLE `OrderItem`
ADD FOREIGN KEY (`OrderNumber`) REFERENCES `Order` (`OrderNumber`),
ADD FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`),
ADD FOREIGN KEY (`DepotItemID`) REFERENCES `DepotItem` (`DepotItemID`),
ADD FOREIGN KEY (`ItemMaterialID`) REFERENCES `ItemMaterial` (`ItemMaterialID`),
ADD FOREIGN KEY (`ItemColourID`) REFERENCES `ItemColour` (`ItemColourID`);

ALTER TABLE `DepotItem`
ADD FOREIGN KEY (`DepotID`) REFERENCES `Depot` (`DepotID`)
ON DELETE CASCADE;

ALTER TABLE `DepotItem`
ADD FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`);

ALTER TABLE `ItemColour`
ADD FOREIGN KEY (`ColourID`) REFERENCES `Colour` (`ColourID`);

ALTER TABLE `ItemColour`
ADD FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`);

ALTER TABLE `ItemMaterial`
ADD FOREIGN KEY (`MaterialID`) REFERENCES `Material` (`MaterialID`);

ALTER TABLE `ItemMaterial`
ADD FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`);
