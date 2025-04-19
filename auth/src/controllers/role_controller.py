from flask.views import MethodView
from flask import request
from src.services.role_service import RoleService
from src.utils.serializers import CreateRole
from src.utils.http_response import http_response


class RoleController(MethodView):
    
    def __init__(self):
        self.service = RoleService()
        
    def list(self):
        roles = self.service.GetAll()
        return http_response(roles.status_code, roles.message, roles.data, roles.error)   
    
    def retrieve(self, id=None):
        role = self.service.GetById(id)
        return http_response(role.status_code, role.message, role.data, role.error)

    def create(self):
        data = CreateRole(**request.json)
        role = self.service.create(data)
        return http_response(role.status_code, role.message, role.data, role.error)

    def update(self, id=None):
        data = CreateRole(**request.json)
        role = self.service.update(data, id)
        return http_response(role.status_code, role.message, role.data, role.error)

    def delete(self, id=None):
        role_deleted = self.service.delete(id)
        return http_response(role_deleted.status_code, role_deleted.message, role_deleted.data, role_deleted.error)