from flask import Blueprint
from src.controllers.role_controller import RoleController

role_bp = Blueprint("roles", __name__)

role_api = RoleController()

role_bp.add_url_rule('/', view_func=role_api.list, methods=['GET'])
role_bp.add_url_rule('/<int:id>', view_func=role_api.retrieve, methods=['GET'])
role_bp.add_url_rule('/create', view_func=role_api.create, methods=['POST'])
role_bp.add_url_rule('/update/<int:id>', view_func=role_api.update, methods=['PUT'])
role_bp.add_url_rule('/delete/<int:id>', view_func=role_api.delete, methods=['DELETE'])
