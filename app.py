from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Joe in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://joes_database_user:OZnyo4u2sOfojDFonBPWKhQ75gGrZYFt@dpg-d48jgvm3jp1c73ck6n6g-a/joes_database")
    conn.close()
    return "Database initiated successfully"

@app.route('/db_create')
def testers():
    conn = psycopg2.connect("postgresql://joes_database_user:OZnyo4u2sOfojDFonBPWKhQ75gGrZYFt@dpg-d48jgvm3jp1c73ck6n6g-a/joes_database")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
                );
                ''')
    conn.commit()
    conn.close()
    return "Basketball table successfullly created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://joes_database_user:OZnyo4u2sOfojDFonBPWKhQ75gGrZYFt@dpg-d48jgvm3jp1c73ck6n6g-a/joes_database")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selected():
    conn = psycopg2.connect("postgresql://joes_database_user:OZnyo4u2sOfojDFonBPWKhQ75gGrZYFt@dpg-d48jgvm3jp1c73ck6n6g-a/joes_database")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def dropper():
    conn = psycopg2.connect("postgresql://joes_database_user:OZnyo4u2sOfojDFonBPWKhQ75gGrZYFt@dpg-d48jgvm3jp1c73ck6n6g-a/joes_database")
    cur = conn.cursor()
    cur.execute('''
                DROP TABLE Basketball;''')
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"

