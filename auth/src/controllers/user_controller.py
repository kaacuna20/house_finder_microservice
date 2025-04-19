from flask.views import MethodView
from flask import request
from src.services.users_service import UserService
from src.utils.serializers import CreateUser, UpdateUser
from src.utils.http_response import http_response

class UserController(MethodView):
    
    def __init__(self):
        self.service = UserService()
        
    def list(self):
        users = self.service.GetAll()
        return http_response(users.status_code, users.message, users.data, users.error)
    
    def retrieve(self, id=None):
        user = self.service.GetById(id)
        return http_response(user.status_code, user.message, user.data, user.error)

    def create(self):
        data = CreateUser(**request.json)
        user = self.service.create(data)
        return http_response(user.status_code, user.message, user.data, user.error)

    def update(self, id):
        data = UpdateUser(**request.json)
        user = self.service.update(data, id)
        return http_response(user.status_code, user.message, user.data, user.error)

    def delete(self, id):
        user_deleted = self.service.delete(id)
        return http_response(user_deleted.status_code, user_deleted.message, user_deleted.data, user_deleted.error)