import os

from flask import Flask
from mysql_pool import MySQLPool

from .views.account import account_blueprint
from .views.booking import booking_blueprint
from .views.organization import organization_blueprint
from .views.parking import parking_blueprint
from .views.payment import payment_blyeprint
from .views.vehicle import vehicle_blueprint

app: Flask = Flask(__name__)

app.register_blueprint(account_blueprint, url_prefix="/accounts")
app.register_blueprint(booking_blueprint, url_prefix="/bookings")
app.register_blueprint(organization_blueprint, url_prefix="/organizations")
app.register_blueprint(parking_blueprint, url_prefix="/parkings")
app.register_blueprint(payment_blyeprint, url_prefix="/payments")
app.register_blueprint(vehicle_blueprint, url_prefix="/vehicles")

mysql_pool = MySQLPool(
    os.getenv('MYSQL_HOST'),
    os.getenv('MYSQL_USER'),
    os.getenv('MYSQL_PASSWORD'),
    os.getenv('MYSQL_DATABASE')
)
