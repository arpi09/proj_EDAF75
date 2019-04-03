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

        return 'OK' + '\n'


@app.route('/ingredients', methods=['GET'])
def ingredients():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    query = "SELECT * FROM ingredients"
    print(query)
    result = cursor.execute(query).fetchall()

    return json.dumps(result, indent=4) + '\n'


@app.route('/pallets', methods=['POST'])
def pallets():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    cookie = request.args.get('cookie')

    query = """INSERT INTO pallets (production_date, blocked, cookie_name, order_id)
    VALUES ( date('now'), 0, \"{}\", NULL )""".format(cookie)
    print(query)
    result = cursor.execute(query).fetchall()

    return json.dumps(result, indent=4) + '\n'


@app.route('/movies')
def movies():
    connection = sqlite3.connect("data.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    title = request.args.get('title')
    year = request.args.get('year')


    if title is not None or year is not None:
        print(title)
        print(year)

        query = "SELECT * FROM movie WHERE prodYear={} AND title=\"{}\"".format(year, title)
        print(query)
        result = cursor.execute(query).fetchall()

    else:
        print("asdasdasd")
        query = """
                    SELECT  *
                    FROM    movie
                """
        result = cursor.execute(query).fetchall()

    connection.commit()
    connection.close()

    return json.dumps(result, indent=4) + '\n'


@app.route('/movies/<IMDBKey>')
def imdbkey(IMDBKey):
    connection = sqlite3.connect("database.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    query = "SELECT * FROM movie WHERE IMDBKey=\"{}\"".format(IMDBKey)
    print(query)
    result = cursor.execute(query).fetchall()

    return json.dumps(result, indent=4) + '\n'


@app.route('/performances', methods=['POST', 'GET'])
def add_screening():

    if request.method == 'POST':
        connection = sqlite3.connect("database.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()

        startTime = request.args.get('time')
        startDate = request.args.get('date')
        movie_IMDBKey = request.args.get('imdb')
        theater_name = request.args.get('theater')


        print(startTime)
        print(startDate)
        print(movie_IMDBKey)
        print(theater_name)
        check_cursor_one = connection.cursor()
        check_cursor_two = connection.cursor()

        query_one = "SELECT * FROM theater WHERE name = '{}';".format(theater_name)
        print(query_one)
        result_one = check_cursor_one.execute(query_one).fetchall()
        print("result =")
        print(result_one)

        query_two = "SELECT * FROM movie WHERE IMDBKey = '{}';".format(movie_IMDBKey)
        print(query_two)
        result_two = check_cursor_two.execute(query_two).fetchall()
        print("result =")
        print(result_two)

        if result_one and result_two:
            query = """ INSERT INTO screening (startTime,  startDate, movie_IMDBKey, theater_name)
                        VALUES ('{}', '{}', '{}','{}');""".format(startTime, startDate, movie_IMDBKey, theater_name)
            cursor.execute(query)
            connection.commit()
            insert_curs = connection.cursor()

            query_insert = "SELECT performance_id FROM screening WHERE rowid=last_insert_rowid()"
            print(query_insert)
            result = insert_curs.execute(query_insert).fetchall()


            connection.commit()
            connection.close()

            return json.dumps(result, indent=4) + '\n'
        else:
            return "Filmen eller bion finns inte.\n"



    if request.method == 'GET':
        connection = sqlite3.connect("database.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        #create_cursor = connection.cursor()


        # temp_table = """CREATE TABLE ticket_nbr (
        #                 performance_id  TEXT,
        #                 nbr_seats       INT,
        #                 PRIMARY KEY (performance_id),
        #                 FOREIGN KEY (performance_id) REFERENCES screening (performance_id)
        # );
        # """

        #create_cursor.execute(temp_table)

        #performance_query = ""















@app.route('/tickets', methods=['POST'])
def add_tickets():
    if request.method == 'POST':
        connection = sqlite3.connect("database.db")
        connection.row_factory = dict_factory
        insert_cursor = connection.cursor()
        pwd_cursor = connection.cursor()
        ticket_cursor = connection.cursor()
        performance_cursor = connection.cursor()

        user = request.args.get('user')
        performance = request.args.get('performance')
        pwd = request.args.get('pwd')

        performance_query = "SELECT * FROM screening WHERE performance_id = '{}'".format(performance)
        performance_result = performance_cursor.execute(performance_query).fetchall()
        print(performance_result)

        if not performance_result:
            return "Error!"


        pwd_hash = hash(pwd)
        print(pwd_hash)

        pwd_query = "SELECT password FROM customer WHERE userName = '{}' AND password = '{}'".format(user, pwd_hash)
        print(pwd_query)

        pwd_result = pwd_cursor.execute(pwd_query).fetchall()

        if not pwd_result:
            return "Wrong password!\n"




        nbr_seats_left = nbr_seats(performance)
        print(nbr_seats_left)
        if nbr_seats_left < 1:
            return "There are no available seats!"


        insert_query = "INSERT INTO ticket (customer_name, performance_id) VALUES ('{}', '{}');".format(user, performance)
        print(insert_query)
        insert_cursor.execute(insert_query)
        connection.commit()

        ticket_query = "SELECT ti_id FROM ticket WHERE rowid=last_insert_rowid()"
        ticket_result = ticket_cursor.execute(ticket_query).fetchall()
        print("ASIDJAIOSDJASOIDJ")
        print(ticket_result)


        return "/tickets/" + ticket_result[0]['ti_id'] + '\n'



@app.route('/customers/<customer_id>/tickets', methods=['GET'])
def get_customer_ticket(customer_id):
    if request.method == 'GET':
        connection = sqlite3.connect("database.db")
        connection.row_factory = dict_factory
        cursor = connection.cursor()

        query = """SELECT startDate AS date, startTime, theater_name AS theater, title, prodYear AS year, count() AS nbrOfTickets
                        FROM ticket
                        JOIN screening
                        USING(performance_id)
                        JOIN movie
                        ON screening.movie_IMDBKey = movie.IMDBKey
                        WHERE customer_name = '{}'
                        GROUP BY performance_id""".format(customer_id)

        result = cursor.execute(query).fetchall()

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
