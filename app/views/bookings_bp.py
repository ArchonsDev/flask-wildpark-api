from flask import Blueprint, request, jsonify
from ..service import BookingService as booking_service

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/ping')
def hello():
    return "pong!"

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

        result, status_code = booking_service.create_booking(date, parking_area_id, vehicle_id, booker_id)
        return jsonify(result), status_code
    
    else:
        return "Unsupported method", 405

@bookings_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def booking(id):
    if request.method == "GET":
        booking = booking_service.get_booking_by_id(id)
        if booking:
            return jsonify(booking), 200
        return jsonify({"error": "Booking not found"}), 404
    
    elif request.method == "PUT":
        booking_service.update_booking(id)
        return jsonify({"message" : "Booking paid successfully"}), 200
    
    elif request.method == "DELETE":
        is_deleted = booking_service.delete_booking(id)
        if is_deleted:
            return jsonify({"message" : "Booking deleted successfully"}), 200
        return jsonify({"error" : "Booking could not be found or deleted"}), 404
    
    else:
        return "Unsupported method", 405