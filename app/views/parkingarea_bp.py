from flask import Blueprint, request, jsonify

from ..service import ParkingareaService as park_service

parkingarea_bp = Blueprint('parkingarea', __name__)

@parkingarea_bp.route('/ping')
def ping():
    return "pong!"

@parkingarea_bp.route("/<id>", methods=["DELETE"])
def parkingarea(id):
    if request.method == "DELETE":
        success = park_service.delete_parkingarea(id)
        
        if success:
            return jsonify({"message": f"Parking area with ID {id} deleted successfully"}), 200
        else:
            return jsonify({"message": f"Failed to delete parking area with ID {id}"}), 500
    else:
        return "Unsupported method", 405