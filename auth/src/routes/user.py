from flask import Blueprint
from src.controllers.user_controller import UserController

user_bp = Blueprint("users", __name__)

user_api = UserController()

user_bp.add_url_rule('/', view_func=user_api.list, methods=['GET'])
user_bp.add_url_rule('/<int:id>', view_func=user_api.retrieve, methods=['GET'])
user_bp.add_url_rule('/create', view_func=user_api.create, methods=['POST'])
user_bp.add_url_rule('/update/<int:id>', view_func=user_api.update, methods=['PUT'])
user_bp.add_url_rule('/delete/<int:id>', view_func=user_api.delete, methods=['DELETE'])