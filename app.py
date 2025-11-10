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