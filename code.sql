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

@app.route('/reset')
def reset():
    connection = sqlite3.connect("database.db")

    del_curs = connection.cursor()

    query_delete = """
                DELETE FROM Pallets;
                DELETE FROM Orders;
                DELETE FROM Customers;
                DELETE FROM Cookies;
                DELETE FROM Order_contents;
                DELETE FROM Cookie_contents;
                DELETE FROM Ingredients;
            """

    del_curs.executescript(query_delete)


    insert_curs = connection.cursor()

    query_insert = """
                INSERT INTO customers (Customer_name, Customer_address)
                VALUES ( 'Finkakor AB',   'Helsingborg'  ),
                       ( 'Småbröd AB',    'Malmö'        ),
                       ( 'Kaffebröd AB',  'Landskrona'   ),
                       ( 'Bjudkakor AB',  'Ystad'        ),
                       ( 'Kalaskakor AB', 'Trelleborg'   ),
                       ( 'Partykakor AB', 'Kristianstad' ),
                       ( 'Gästkakor AB',  'Hässleholm'   ),
                       ( 'Skånekakor AB', 'Perstorp'     );

                INSERT INTO cookies (Cookie_name)
                VALUES  ( 'Nut ring'      ),
                        ( 'Nut cookie'    ),
                        ( 'Amneris'       ),
                        ( 'Tango'         ),
                        ( 'Almond delight'),
                        ( 'Berliner'      );

               INSERT INTO ingredients ( Ingredient_name, Unit , Storage_amount, Last_delivery_date, Last_delivery_amount)
               VALUES   ( 'Flour',                 'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Butter',                'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Icing sugar',           'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Roasted, chopped nuts', 'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Fine-ground nuts',      'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Ground, roasted nuts',  'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Bread crumbs',          'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Sugar',                 'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Egg whites',            'ml',    100 000,    GETDATE ( ),   100 000),
                        ( 'Chocolate',             'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Marzipan',              'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Eggs',                  'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Potato starch',         'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Wheat flour',           'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Sodium bicarbonate',    'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Vanilla',               'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Chopped almonds',       'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Cinnamon',              'g',     100 000,    GETDATE ( ),   100 000),
                        ( 'Vanilla sugar',         'g',     100 000,    GETDATE ( ),   100 000);

               INSERT INTO cookie_contents ( Ingredient_amount, Cookie_name, Ingredient_name)
               VALUES   ( 450,   'Nut ring',    'Flour'                 ),
                        ( 450,   'Nut ring',    'Butter'                ),
                        ( 190,   'Nut ring',    'Icing sugar'           ),
                        ( 225,   'Nut ring',    'Roasted, chopped nuts' ),
                        ( 750,   'Nut cookie',  'Fine-ground nuts'      ),
                        ( 625,   'Nut cookie',  'Ground, roasted nuts'  ),
                        ( 125,   'Nut cookie',  'Bread crumbs'          ),
                        ( 375,   'Nut cookie',  'Sugar'                 ),
                        ( 350,   'Nut cookie',  'Egg whites'            ),
                        ( 50,    'Nut cookie',  'Chocolate'             ),
                        ( 750,   'Amneris',     'Marzipan'              ),
                        ( 250,   'Amneris',     'Butter'                ),
                        ( 250,   'Amneris',     'Eggs'                  ),
                        ( 25,    'Amneris',     'Potato starch'         ),
                        ( 25,    'Amneris',     'Wheat flour'           ),
                        ( 200,   'Tango',       'Butter'                ),
                        ( 250,   'Tango',       'Sugar'                 ),
                        ( 300,   'Tango',       'Flour'                 ),
                        ( 4,     'Tango',       'Sodium bicarbonate'    ),
                        ( 2,     'Tango',       'Vanilla'               ),
                        ( 400,   'Almond',      'Butter'                ),
                        ( 270,   'Almond',      'Sugar'                 ),
                        ( 279,   'Almond',      'Chopped almonds'       ),
                        ( 400,   'Almond',      'Flour'                 ),
                        ( 10,    'Almond',      'Cinnamon'              ),
                        ( 350,   'Berliner',    'Flour'                 ),
                        ( 250,   'Berliner',    'Butter'                ),
                        ( 100,   'Berliner',    'Icing sugar'           ),
                        ( 50,    'Berliner',    'Eggs'                  ),
                        ( 5,     'Berliner',    'Vanilla sugar'         ),
                        ( 50,    'Berliner',    'Chocolate'             );


            """.format(hash("dobido"),hash("whatsinaname"))

    insert_curs.executescript(query_insert)

    return 'OK'


