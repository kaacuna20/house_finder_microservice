from flask import request
from flask.views import MethodView
from src.services.municipality_service import MunicipalityService
from src.utils.serializers import CreateMunicipality
from src.utils.http_response import http_response


class MunicipalityController(MethodView):
    def __init__(self):
        self.service = MunicipalityService()
        
    def list(self):
        municipalities = self.service.getAll()
        return http_response(municipalities.status_code, municipalities.message, municipalities.data, municipalities.error)
    
    def retrieve(self, param=None):
        municipality = self.service.getByCode(param)
        return http_response(municipality.status_code, municipality.message, municipality.data, municipality.error)
    
    def create(self):
        data = CreateMunicipality(**request.json)
        municipality = self.service.create(data)
        return http_response(municipality.data, municipality.status_code, municipality.message, municipality.error)
    
    def update(self, id=None):
        data = CreateMunicipality(**request.json)
        municipality = self.service.update(id, data)
        return http_response(municipality.data, municipality.status_code, municipality.message, municipality.error)
    
    def delete(self, id=None):
        municipality_deleted = self.service.delete(id)
        return http_response(municipality_deleted.data, municipality_deleted.status_code, municipality_deleted.message, municipality_deleted.error)