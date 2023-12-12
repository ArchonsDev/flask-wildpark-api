from flask import Flask

from mysql_pool import MySQLPool

app = Flask(__name__)
app.config["conn"] = MySQLPool()

with app.config.get("conn") as conn:
    c = conn.cursor()
    c.execute("SHOW TABLES")
    result = c.fetchall()

    tables = result if result else []
    
    if not ("tblaccount",) in tables:
        with open("./sql/01_tblaccount.sql", "r") as f:
            c.execute(f.read())

    if not ("tblparkingarea",) in tables:
        with open("./sql/05_tblparkingarea.sql") as f:
            c.execute(f.read())

    if not ("tblvehicle",) in tables:
        with open("./sql/06_tblvehicle.sql", "r") as f:
            c.execute(f.read())

    if not ("tblbooking",) in tables:
        with open("./sql/08_tblbooking.sql", "r") as f:
            c.execute(f.read())

if __name__ == "__main__":
    app.run()
