from flask import Blueprint
from src.controllers.permission_controller import PermisionController


permission_bp = Blueprint('permission', __name__)

permission_api = PermisionController()

permission_bp.add_url_rule('/role/<string:param>', view_func=permission_api.list_by_role, methods=['GET'])
permission_bp.add_url_rule('/reference/<string:param>', view_func=permission_api.list_by_reference, methods=['GET'])
permission_bp.add_url_rule('/create', view_func=permission_api.create, methods=['POST'])
permission_bp.add_url_rule('/update/<int:id>', view_func=permission_api.update, methods=['PUT'])
permission_bp.add_url_rule('/delete/<int:id>', view_func=permission_api.delete, methods=['DELETE'])