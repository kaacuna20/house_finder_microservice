from flask.views import MethodView
from flask import request
from src.services.permission_service import PermisionService
from src.utils.serializers import CreatePermision
from src.utils.http_response import http_response


class PermisionController(MethodView):
    
    def __init__(self):
        self.service = PermisionService()
        
    def list_by_role(self, param=None):
        permisions = self.service.get_permissions_by_role(param)
        return http_response(permisions.status_code, permisions.message, permisions.data, permisions.error)
        
    def list_by_reference(self, param=None):
        permision = self.service.get_permissions_by_reference(param)
        return http_response(permision.status_code, permision.message, permision.data, permision.error)
        
    def create(self):
        data = CreatePermision(**request.json)
        permision = self.service.create(data)
        return http_response(permision.status_code, permision.message, permision.data, permision.error)

    def update(self, id=None):
        data = CreatePermision(**request.json)
        permision = self.service.update(data, id)
        return http_response(permision.status_code, permision.message, permision.data, permision.error)
        
    def delete(self, id=None):
        permission_deleted = self.service.delete(id)
        return http_response(permission_deleted.status_code, permission_deleted.message, permission_deleted.data, permission_deleted.error)    