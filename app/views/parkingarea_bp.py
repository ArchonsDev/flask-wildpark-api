from flask import Blueprint, request, jsonify
from ..service import ParkingareaService as park_service

parkingarea_bp = Blueprint('parkingarea', __name__)

@parkingarea_bp.route('/ping')
def ping():
    return "pong!"

@parkingarea_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return park_service.get_all_parkingarea()
    elif request.method == 'POST':
        data = request.json
        required_fields = ["slots"]
        
        if not all(field in data for field in required_fields):
            return jsonify({"message": "Missing required fields"}), 400
        
        try:
            slots = data["slots"]
            park_service.add_parkingarea(slots,)
            return jsonify({"message": "Parking area added successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Failed to add parking area. Error: {str(e)}"}), 500
        
    else:
        return 'Unsupported method', 405

@parkingarea_bp.route("/<parking_area_id>", methods=["GET","PUT", "DELETE"])
def parkingarea(parking_area_id):
    if request.method == "GET":
        parking_area = park_service.get_parkingarea_by_id(parking_area_id)
        
        if parking_area:
            return jsonify({"parking_area": parking_area}), 200
        else:
            return jsonify({"message": f"Parking area with ID {parking_area_id} not found"}), 404
    
    elif request.method == "PUT":
        data = request.json
        slots = data.get("slots")

        success = park_service.update_parkingarea(parking_area_id, slots)

        if success:
            return jsonify({"message": f"Parking area with ID {parking_area_id} updated successfully"}), 200
        else:
            return jsonify({"message": f"Failed to update parking area with ID {parking_area_id}"}), 500
    elif request.method == "DELETE":
        success = park_service.delete_parkingarea(parking_area_id)

        if success:
            return jsonify({"message": f"Parking area with ID {parking_area_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"Failed to delete parking area with ID {parking_area_id}"}), 500
    else:
        return "Unsupported method", 405
