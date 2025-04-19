from flask import Blueprint
from src.controllers.project_user_controller import ProjectUserQualificationController


project_user_bp = Blueprint("project_user", __name__)
project_user_api = ProjectUserQualificationController()

project_user_bp.add_url_rule('/', view_func=project_user_api.list, methods=['GET'])
project_user_bp.add_url_rule('/create', view_func=project_user_api.create, methods=['POST'])
project_user_bp.add_url_rule('/delete/<int:id>', view_func=project_user_api.delete, methods=['DELETE'])