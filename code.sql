-- Delete the tables if they exist.
-- Disable foreign key checks, so the tables can
-- be dropped in arbitrary order.
PRAGMA foreign_keys=OFF;

DROP TABLE IF EXISTS pallets;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS cookies;
DROP TABLE IF EXISTS order_contents;
DROP TABLE IF EXISTS cookie_contents;
DROP TABLE IF EXISTS ingredients;

PRAGMA foreign_keys=ON;

--------------------------------------------------------------
CREATE TABLE pallets (
Pallet_number                 INT,
Production_date               DATE  NOT NULL,
Production_time               TIME  NOT NULL,
blocked                       BIT   DEFAULT 0,

Cookie_name                   TEXT  NOT NULL,
Order_id                      INT   DEFAULT NULL,

PRIMARY KEY (Pallet_number),
FOREIGN KEY (Cookie_name)     REFERENCES  cookies(Cookie_name),
FOREIGN KEY (Order_id)        REFERENCES  orders(Order_id)
);


--------------------------------------------------------------
CREATE TABLE orders (
Order_id                      INT,
Date_to_be_delivered          DATE  NOT NULL,
Delivered_status              BIT   NOT NULL,

Customer_name                 TEXT  NOT NULL,

PRIMARY KEY (Order_id),
FOREIGN KEY (Customer_name)   REFERENCES  customers(Customer_name)
);


--------------------------------------------------------------
CREATE TABLE customers (
Customer_name                 TEXT,
Customer_address              TEXT  NOT NULL,

PRIMARY KEY (Customer_name)
);


--------------------------------------------------------------
CREATE TABLE cookies (
Cookie_name                   TEXT,

PRIMARY KEY (Cookie_name)
);


--------------------------------------------------------------
CREATE TABLE order_contents (
Order_amount                  INT,

Order_id                      INT   NOT NULL,
Cookie_name                   TEXT  NOT NULL,

FOREIGN KEY (Order_id)        REFERENCES  orders(Order_id),
FOREIGN KEY (Cookie_name)     REFERENCES  cookies(Cookie_name)
);


--------------------------------------------------------------
CREATE TABLE cookie_contents (
Ingredient_amount             INT,

Cookie_name                   TEXT  NOT NULL,
Ingredient_name               TEXT  NOT NULL,

FOREIGN KEY (Cookie_name)     REFERENCES  cookies(Cookie_name),
FOREIGN KEY (Ingredient_name) REFERENCES  ingredients(Ingredient_name)
);


--------------------------------------------------------------
CREATE TABLE ingredients (
Ingredient_name               TEXT,
Unit                          TEXT,
Storage_amount                INT   NOT NULL,
Last_delivery_date            DATE,
Last_delivery_amount          INT,

PRIMARY KEY (Ingredient_name)
);




-- Insert data into the tables.
