from flask import Blueprint, request, jsonify
from ..service import BookingService as booking_service

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/')
def hello():
    return "Hello World!"

@bookings_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return booking_service.get_all_bookings()
    elif request.method == 'POST':
        data = request.json
        date = data.get("date")
        parking_area_id = data.get("parking_area_id")
        vehicle_id = data.get("vehicle_id")
        booker_id = data.get("booker_id")

        booking_service.create_booking(date, parking_area_id, vehicle_id, booker_id)
        return jsonify({"message" : "Booking created successfully"}), 200
    else:
        return "Unsupported method", 405

@bookings_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def booking(id):
    if request.method == "GET":
        return booking_service.get_booking_by_id(id)
    elif request.method == "PUT":
        data = request.json
        booking_service.update_booking(id, data)
        return jsonify({"message" : "Booking updated successfully"}), 200
    elif request.method == "DELETE":
        return booking_service.delete_booking(id)
    else:
        return "Unsupported method", 405