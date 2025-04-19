from flask import request
from flask.views import MethodView
from src.services.sync_service import SyncService
from src.utils.http_response import http_response


class SyncController(MethodView):
    
    def __init__(self):
        self.service = SyncService()
        
    def sync(self):
        """
        Sync data with the gateway service.
        """
        response = self.service.sync_projects(request)
        return http_response(response.status_code, response.message, response.data, response.error)