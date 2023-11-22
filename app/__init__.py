import os

from flask import Flask
from mysql_pool import MySQLPool

app: Flask = Flask(__name__)

mysql_pool = MySQLPool(
    os.getenv('MYSQL_HOST'),
    os.getenv('MYSQL_USER'),
    os.getenv('MYSQL_PASSWORD'),
    os.getenv('MYSQL_DATABASE')
)
