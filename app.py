from flask import Flask, render_template, jsonify, request
import json
import sqlite3
import hashlib
from datetime import datetime

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
                INSERT INTO customers (customer_name, customer_address)
                VALUES ( 'Finkakor AB',   'Helsingborg'  ),
                       ( 'Småbröd AB',    'Malmö'        ),
                       ( 'Kaffebröd AB',  'Landskrona'   ),
                       ( 'Bjudkakor AB',  'Ystad'        ),
                       ( 'Kalaskakor AB', 'Trelleborg'   ),
                       ( 'Partykakor AB', 'Kristianstad' ),
                       ( 'Gästkakor AB',  'Hässleholm'   ),
                       ( 'Skånekakor AB', 'Perstorp'     );

                INSERT INTO cookies (cookie_name)
                VALUES  ( 'Nut ring'      ),
                        ( 'Nut cookie'    ),
                        ( 'Amneris'       ),
                        ( 'Tango'         ),
                        ( 'Almond delight'),
                        ( 'Berliner'      );

               INSERT INTO ingredients ( ingredient_name, Unit , storage_amount, last_delivery_date, last_delivery_amount)
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

               INSERT INTO cookie_contents ( ingredient_amount, cookie_name, ingredient_name)
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

        return json.dumps({"status": "ok"})

@app.route('/customers')
def customers ():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    
    query =     """
        SELECT customer_name as name, customer_address as address 
        FROM customers
    """
    
    result = cursor.execute(query).fetchall()
    result = {"customers": result}
    # print(json.dumps(result, indent=4) + '\n')
    return json.dumps(result, indent=4) + '\n'



@app.route('/recipes')
def recipes ():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    
    query =     """
        SELECT Cookie_name, Ingredient_name, Ingredient_amount, Unit
        FROM cookie_contents
        JOIN ingredients
        USING(Ingredient_name)
        ORDER BY Cookie_name, Ingredient_name
    """
    
    result = cursor.execute(query).fetchall()
    result = {"recipes": result}
    return json.dumps(result, indent=4) + '\n'


@app.route('/ingredients', methods=['GET'])
def ingredients():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    query = """
        SELECT ingredient_name AS name, storage_amount AS quantity, unit 
        FROM ingredients
    """

    result = cursor.execute(query).fetchall()
    result = {"ingredients": result}
    return json.dumps(result, indent=4) + '\n'


@app.route('/pallets', methods=['POST'])
def POST_pallets():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    cookie = request.args.get('cookie')

    test1 = """
        SELECT cookie_name
        FROM cookies
        WHERE cookie_name =  ?
    """
    
    # params = 
    test1_result = cursor.execute(test1, [cookie]).fetchall()
    # print(test1_result)
    if not test1_result:
        return json.dumps({"status":"no such cookie"})

    test2 = """
        SELECT name, available, cost
        FROM

            (SELECT ingredient_name AS name, ingredient_amount AS cost
            FROM cookie_contents
            WHERE cookie_name =  ?)

        LEFT JOIN

            (SELECT ingredient_name AS name, storage_amount AS available
            FROM ingredients
            JOIN cookie_contents
                USING( ingredient_name)
            WHERE cookie_name =  ?)

        USING(name)

    WHERE ((54 * cost) > available) OR (available is NULL)
    """

    test2_result = cursor.execute(test2, [cookie, cookie]).fetchall()
    if  test2_result:
        return json.dumps({"status":"not enough ingredients"})
    
    cursor = connection.cursor()

    query_two = """SELECT ingredient_name, ingredient_amount
    FROM cookie_contents
    WHERE cookie_name = ?"""

    result2 = cursor.execute(query_two,[cookie]).fetchall()
    for item in result2:
        query_three = """
            UPDATE ingredients
            SET storage_amount = storage_amount - ?*54
            WHERE ingredient_name = ?
        """
        
        cursor.execute(query_three, [item['ingredient_amount'], item['ingredient_name']])


    query = """
    INSERT INTO pallets (production_date, blocked, cookie_name, order_id)
        VALUES ( date('now'), 0, ?, NULL )
    """
    cursor.execute(query, [cookie])

    queryid = """
            SELECT pallet_number
            FROM pallets
            WHERE rowid = last_insert_rowid()
    """

    result = cursor.execute(queryid).fetchall()
    connection.commit()
    ans = {"status": "ok", "id": ""}
    ans["id"] = result[0]['pallet_number']
    connection.close()
    return json.dumps(ans)


@app.route('/pallets', methods=['GET'])
def GET_pallets():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    
    if request.args.get('cookie'):
        cookie = request.args.get('cookie')
        blocked = request.args.get('blocked')
        if request.args.get('after'):
            date = request.args.get('after')
        else:
            date = request.args.get('before')

        # query = """
        #     SELECT Pallet_number AS id,  Cookie_name AS cookie, Production_date AS productionDate,
        #     Customer_name AS customer, CASE WHEN blocked = 0 THEN 'false' ELSE 'true' END AS blocked
        #     FROM pallets
        #     LEFT JOIN orders
        #         USING(Order_id)
        #     WHERE cookie=? AND blocked={} AND production_date>?
        # """
        query = """
            SELECT Pallet_number AS id,  Cookie_name AS cookie, Production_date AS productionDate,
            Customer_name AS customer, blocked
            FROM pallets
            LEFT JOIN orders
                USING(Order_id)
            WHERE cookie=? AND blocked={} AND production_date>?
        """
        
        result = cursor.execute(query, [cookie, blocked, date] ).fetchall()
        connection.commit()
        connection.close()
    else:
        query = """
            SELECT Pallet_number AS id,  Cookie_name AS cookie, Production_date AS productionDate,
            Customer_name AS customer, blocked
            FROM pallets
            LEFT JOIN orders
                USING(Order_id)
        """
        
        result = cursor.execute(query).fetchall()
        connection.commit()
        connection.close()

    result = {"pallets": result}
    return json.dumps(result, indent=4) + '\n'


@app.route('/cookies', methods=['GET'])
def cookies():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    
    query = """
        SELECT cookie_name AS name
        FROM cookies
        ORDER BY name
    """
    
    result = cursor.execute(query).fetchall()
    connection.commit()
    connection.close()
    result = {"cookies": result}
    return (json.dumps(result, indent=4) + '\n')


@app.route('/block/<cookie_name>/<from_date>/<to_date>', methods=['POST'])
def block(cookie_name, from_date, to_date):
        connection = sqlite3.connect("data.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()

        query = """
                UPDATE pallets
                SET blocked = 1
                WHERE cookie_name = ? AND production_date BETWEEN ? AND ? 
        """

        result = cursor.execute(query, [cookie_name, from_date, to_date]).fetchall()
        connection.commit()
        connection.close()
        return json.dumps(result, indent=4) + '\n'


@app.route('/unblock/<cookie_name>/<from_date>/<to_date>', methods=['POST'])
def unblock(cookie_name, from_date, to_date):

        connection = sqlite3.connect("data.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()

        query = """
                UPDATE pallets
                SET blocked = 0
                WHERE cookie_name = ? AND production_date BETWEEN ? AND ? 
        """


        # print(query)
        result = cursor.execute(query, [cookie_name, from_date, to_date]).fetchall()
        connection.commit()
        connection.close()

        return json.dumps({"status": "ok"})
        # return json.dumps(result, indent=4 + '\n'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def hash(msg):
    return hashlib.sha256(msg.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    app.run(port=8888)
