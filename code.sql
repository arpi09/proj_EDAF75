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
pallet_number                 INT   DEFAULT (lower(hex(randomblob(16)))),
production_date               DATE  NOT NULL,
blocked                       BIT   DEFAULT 0,

cookie_name                   TEXT  NOT NULL,
order_id                      INT   DEFAULT NULL,

PRIMARY KEY (pallet_number),
FOREIGN KEY (cookie_name)     REFERENCES  cookies(cookie_name),
FOREIGN KEY (order_id)        REFERENCES  orders(order_id)
);


--------------------------------------------------------------
CREATE TABLE orders (
order_id                      INT   DEFAULT (lower(hex(randomblob(16)))),
date_to_be_delivered          DATE  NOT NULL,
delivered_status              BIT   NOT NULL,

customer_name                 TEXT  NOT NULL,

PRIMARY KEY (order_id),
FOREIGN KEY (customer_name)   REFERENCES  customers(customer_name)
);


--------------------------------------------------------------
CREATE TABLE customers (
customer_name                 TEXT,
customer_address              TEXT  NOT NULL,

PRIMARY KEY (customer_name)
);


--------------------------------------------------------------
CREATE TABLE cookies (
cookie_name                   TEXT,

PRIMARY KEY (cookie_name)
);


--------------------------------------------------------------
CREATE TABLE order_contents (
order_amount                  INT,

order_id                      INT   NOT NULL,
cookie_name                   TEXT  NOT NULL,

FOREIGN KEY (order_id)        REFERENCES  orders(order_id),
FOREIGN KEY (cookie_name)     REFERENCES  cookies(cookie_name)
);


--------------------------------------------------------------
CREATE TABLE cookie_contents (
ingredient_amount             INT,

cookie_name                   TEXT  NOT NULL,
ingredient_name               TEXT  NOT NULL,

FOREIGN KEY (cookie_name)     REFERENCES  cookies(cookie_name),
FOREIGN KEY (ingredient_name) REFERENCES  ingredients(ingredient_name)
);


--------------------------------------------------------------
CREATE TABLE ingredients (
ingredient_name               TEXT,
unit                          TEXT,
storage_amount                INT   NOT NULL,
last_delivery_date            DATE,
last_delivery_amount          INT,

PRIMARY KEY (ingredient_name)
);




-- Insert data into the tables.
