from flask import Flask, render_template, jsonify, request
import json
import sqlite3
import hashlib

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/ping')
def asdsa():
    return 'pong\n'

@app.route('/reset', methods=['POST'])
def reset():
    if request.method == 'POST':
        connection = sqlite3.connect("data.db")

        del_curs = connection.cursor()

        query_delete = """
                    DELETE FROM pallets;
                    DELETE FROM orders;
                    DELETE FROM customers;
                    DELETE FROM cookies;
                    DELETE FROM order_contents;
                    DELETE FROM cookie_contents;
                    DELETE FROM ingredients;
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
               VALUES   ( 'Flour',                 'g',     100000,    date('now'),   100000),
                        ( 'Butter',                'g',     100000,    date('now'),   100000),
                        ( 'Icing sugar',           'g',     100000,    date('now'),   100000),
                        ( 'Roasted, chopped nuts', 'g',     100000,    date('now'),   100000),
                        ( 'Fine-ground nuts',      'g',     100000,    date('now'),   100000),
                        ( 'Ground, roasted nuts',  'g',     100000,    date('now'),   100000),
                        ( 'Bread crumbs',          'g',     100000,    date('now'),   100000),
                        ( 'Sugar',                 'g',     100000,    date('now'),   100000),
                        ( 'Egg whites',            'ml',    100000,    date('now'),   100000),
                        ( 'Chocolate',             'g',     100000,    date('now'),   100000),
                        ( 'Marzipan',              'g',     100000,    date('now'),   100000),
                        ( 'Eggs',                  'g',     100000,    date('now'),   100000),
                        ( 'Potato starch',         'g',     100000,    date('now'),   100000),
                        ( 'Wheat flour',           'g',     100000,    date('now'),   100000),
                        ( 'Sodium bicarbonate',    'g',     100000,    date('now'),   100000),
                        ( 'Vanilla',               'g',     100000,    date('now'),   100000),
                        ( 'Chopped almonds',       'g',     100000,    date('now'),   100000),
                        ( 'Cinnamon',              'g',     100000,    date('now'),   100000),
                        ( 'Vanilla sugar',         'g',     100000,    date('now'),   100000);

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


            """

        insert_curs.executescript(query_insert)

        return 'OK' + '\n'





@app.route('/cookies', methods=['GET'])
def cookies():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    query = """
        select Cookie_name AS name 
        from cookies
    """
    print(query)
    result = cursor.execute(query).fetchall()
    print(result)
    connection.commit()
    connection.close()

    return json.dumps(result, indent=4) + '\n'



@app.route('/pallets', methods=['GET'])
def pallets():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    query = """
        SELECT Pallet_number AS id,  Cookie_name AS cookie, Production_date AS productionDate,
        Customer_name AS customer, blocked
        FROM pallets
        JOIN orders
            USING(Order_id)
    """
    print(query)
    result = cursor.execute(query).fetchall()
    print(result)
    connection.commit()
    connection.close()

    return json.dumps(result, indent=4) + '\n'





def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def hash(msg):
    return hashlib.sha256(msg.encode('utf-8')).hexdigest()


def nbr_seats(performance_id):
    nbr_seats_left = 0
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    query = """
                SELECT  ABS(capacity - count())
                FROM    screening
                LEFT JOIN    theater
                ON      theater.name = screening.theater_name
                LEFT JOIN    ticket
                USING   (performance_id)
                WHERE   performance_id = '{}'
            """.format(performance_id)

    result = cursor.execute(query).fetchall()
    print("asdasdasdasdasdasdasdasdasdads")
    print(query)
    print(result)

    return result[0][0]

if __name__ == '__main__':
    app.run()
