from flask import Blueprint, request, jsonify

from ..service import VehicleService as veh_service

vehicle_bp = Blueprint('vehicle', __name__)

@vehicle_bp.route('/ping')
def ping():
    return "pong!"

@vehicle_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return veh_service.get_all_vehicles()
    elif request.method == 'POST':
        data = request.json
        required_fields = ["color", "make", "model", "plate_number", "owner_id", "parking_area_id"]
        
        if not all(field in data for field in required_fields):
            return jsonify({"message": "Missing required fields"}), 400
        
        try:
            veh_service.add_vehicle(**data)
            return jsonify({"message": "Vehicle Added"}), 201
        except Exception as e:
            return jsonify({"message": f"Failed to add vehicle. Error: {str(e)}"}), 500
        
    else:
        return 'Unsupported method', 405
    
@vehicle_bp.route("/<vehicle_id>", methods=["GET", "PUT", "DELETE"])
def vehicle(vehicle_id):
    if request.method == "GET":
        vehicle_details = veh_service.get_vehicle_by_vehicle_id(vehicle_id)
        
        if vehicle_details:
            return jsonify(vehicle_details), 200
        else:
            return jsonify({"message": "Vehicle not found"}), 404
    elif request.method == "PUT":
        data = request.json
        veh_service.update_vehicle(vehicle_id, data)
        return jsonify({"message": f"Vehicle with ID {vehicle_id} updated successfully"}), 200
    elif request.method == "DELETE":
        success = veh_service.delete_vehicle(vehicle_id)

        if success:
            return jsonify({"message": f"Vehicle with ID {vehicle_id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"Failed to delete vehicle with ID {vehicle_id}"}), 500
    else:
        return "Unsupported method", 405