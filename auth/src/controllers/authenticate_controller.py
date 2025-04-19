from flask.views import MethodView
from flask import request, jsonify
from src.services.authenticate_service import AuthenticateService
from src.utils.serializers import AuthUser, Token
from src.utils.http_response import http_response


class AuthenticateController(MethodView):
    
    def __init__(self):
        self.service = AuthenticateService()
        
    def login(self):
        data = AuthUser(**request.json)
        authenticate = self.service.authenticate(data)
            
        return http_response(
            status_code=authenticate.status_code,
            message=authenticate.message,
            error=authenticate.error,
            data=authenticate.data
        )

        
    def get_user_from_token(self):
        token = Token(**request.json)
        user = self.service.get_user_from_token(token)
        return http_response(
            status_code=user.status_code,
            message=user.message,
            error=user.error,
            data=user.data
        )