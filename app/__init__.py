from flask import Flask

from mysql_pool import mysql_pool
from .views import *

app = Flask(__name__)

with mysql_pool as conn:
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

app.register_blueprint(accounts_bp, url_prefix="/accounts")
app.register_blueprint(vehicle_bp, url_prefix='/vehicle')
app.register_blueprint(parkingarea_bp, url_prefix='/parkingarea')
app.register_blueprint(bookings_bp, url_prefix="/bookings")


if __name__ == "__main__":
    app.run(debug=True)
