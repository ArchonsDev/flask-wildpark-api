from flask import Blueprint

account_blueprint = Blueprint('accounts', __name__)

@account_blueprint.route("/")
def index():
    return "Account index"
