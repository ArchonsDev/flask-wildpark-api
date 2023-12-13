from flask import Blueprint, request, jsonify
from ..service import AccountService as acc_service

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/ping')
def ping():
    return "pong!"

@accounts_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        accounts = acc_service.get_all_accounts()

        return jsonify(accounts), 200
    elif request.method == 'POST':
        data = request.json
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        account = acc_service.create_account(firstname, lastname)

        return jsonify(account.to_dict()), 200
    else:
        return 'Unsupported method', 405
    
@accounts_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def account(id):
    if request.method == "GET":
        account = acc_service.get_account_by_id(id)

        return jsonify(account.to_dict()), 200
    elif request.method == "PUT":
        data = request.json
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        account = acc_service.update_account(id, firstname, lastname)

        return jsonify(account.to_dict())
    elif request.method == "DELETE":
        acc_service.delete_account(id)
        return "Account deleted", 200
    else:
        return "Unsupported method", 405
