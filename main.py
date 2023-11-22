from flask import Flask

from mysql_pool import MySQLPool

app: Flask = Flask(__name__)
app.config["sql"] = MySQLPool()

@app.route("/")
def index() -> str:
    return "Hello, world!"
