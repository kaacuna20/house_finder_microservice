from flask import request
from flask.views import MethodView
from src.services.company_service import CompanyService
from src.utils.serializers import CreateCompany
from src.utils.http_response import http_response


class CompanyController(MethodView):
    
    def __init__(self):
        self.service = CompanyService()
        
    def list(self):
        companies = self.service.getAll()
        return http_response(companies.status_code, companies.message, companies.data, companies.error)
    
    def retrieve(self, param=None):
        company = self.service.getByNit(param)
        return http_response(company.status_code, company.message, company.data, company.error)
    
    def create(self):
        data = CreateCompany(**request.json)
        company = self.service.create(data)
        return http_response(company.status_code, company.message, company.data, company.error)
    
    def update(self, id=None):
        data = CreateCompany(**request.json)
        company = self.service.update(id, data)
        return http_response(company.status_code, company.message, company.data, company.error)
    
    def delete(self, id=None):
        company_deleted = self.service.delete(id)
        return http_response(company_deleted.status_code, company_deleted.message, company_deleted.data, company_deleted.error)