from flask import Blueprint
from src.controllers.authenticate_controller import AuthenticateController

auth_bp = Blueprint("auth", __name__)

auth_api = AuthenticateController()

auth_bp.add_url_rule('/login', view_func=auth_api.login, methods=['POST'])
auth_bp.add_url_rule('/get-user', view_func=auth_api.get_user_from_token, methods=['POST'])