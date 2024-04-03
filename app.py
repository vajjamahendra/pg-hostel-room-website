from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)