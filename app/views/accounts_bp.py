from flask import Blueprint, request, jsonify
from ..service import AccountService as acc_service

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/ping')
def ping():
    return "pong!"

@accounts_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return acc_service.get_all_accounts()
    elif request.method == 'POST':
        data = request.json
        firstname = data.get("firstname")
        lastname = data.get("lastname")

        acc_service.create_account(firstname, lastname)
        return "User created!"
    else:
        return 'Unsupported method', 405
    
@accounts_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def account(id):
    if request.method == "GET":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    else:
        return "Unsupported method", 405