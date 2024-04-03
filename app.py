from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host=""
)



cursor = conn.cursor(cursor_factory=RealDictCursor)

#API for Authentacting the Admin
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')


#API to list all the users
@app.route('/users',methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return jsonify({'results':students})



if __name__ == '__main__':
    app.run(debug=True)