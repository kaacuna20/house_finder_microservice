from flask import Blueprint
from src.controllers.company_controller import CompanyController


company_bp = Blueprint("company", __name__)
company_api = CompanyController()

company_bp.add_url_rule('/', view_func=company_api.list, methods=['GET'])
company_bp.add_url_rule('/<string:param>', view_func=company_api.retrieve, methods=['GET'])
company_bp.add_url_rule('/create', view_func=company_api.create, methods=['POST'])
company_bp.add_url_rule('/update/<int:id>', view_func=company_api.update, methods=['PUT'])
company_bp.add_url_rule('/delete/<int:id>', view_func=company_api.delete, methods=['DELETE'])