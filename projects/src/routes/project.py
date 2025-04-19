from flask import Blueprint
from src.controllers.project_controller import ProjectController


project_bp = Blueprint("projects", __name__)
project_api = ProjectController()

project_bp.add_url_rule('/', view_func=project_api.list, methods=['GET'])
project_bp.add_url_rule('/<string:param>', view_func=project_api.retrieve, methods=['GET'])
project_bp.add_url_rule('/create', view_func=project_api.create, methods=['POST'])
project_bp.add_url_rule('/update/<int:id>', view_func=project_api.update, methods=['PUT'])
project_bp.add_url_rule('/delete/<int:id>', view_func=project_api.delete, methods=['DELETE'])
project_bp.add_url_rule('/sync', view_func=project_api.sync, methods=['POST'])