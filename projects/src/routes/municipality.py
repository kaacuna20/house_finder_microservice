from flask import Blueprint
from src.controllers.municipality_controller import MunicipalityController

municipality_bp = Blueprint("municipality", __name__)
municipality_api = MunicipalityController()

municipality_bp.add_url_rule('/', view_func=municipality_api.list, methods=['GET'])
municipality_bp.add_url_rule('/<string:param>', view_func=municipality_api.retrieve, methods=['GET'])
municipality_bp.add_url_rule('/create', view_func=municipality_api.create, methods=['POST'])
municipality_bp.add_url_rule('/update/<int:id>', view_func=municipality_api.update, methods=['PUT'])
municipality_bp.add_url_rule('/delete/<int:id>', view_func=municipality_api.delete, methods=['DELETE'])