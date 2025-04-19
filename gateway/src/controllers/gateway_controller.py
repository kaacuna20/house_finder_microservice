from flask import request, jsonify
from flask.views import MethodView
from src.services.gateway_service import GatewayService
from src.utils.normalize_path import normalize_route
from src.utils.http_response import http_response


class GatewayController(MethodView):
    """Controller for managing the gateway service."""

    def __init__(self):
        self.service = GatewayService()
        
    def status(self):
        """Check the status of the gateway service."""
        try:
            return jsonify({"msg": "Gateway service is running"}), 200
        except Exception as e:
            return jsonify({"msg": str(e)}), 500

    def proxy(self, path):
        """Proxy request to the appropriate service."""
        response = self.service.proxy(request, path)
        return http_response(response.status_code, response.message, response.data, response.error) 
