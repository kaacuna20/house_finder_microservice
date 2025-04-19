from flask import Blueprint
from src.controllers.gateway_controller import GatewayController


gateway_bp = Blueprint("gateway", __name__)
gateway_api = GatewayController()

gateway_bp.add_url_rule("/", view_func=gateway_api.status, methods=["GET"])
gateway_bp.add_url_rule("/<path:path>", view_func=gateway_api.proxy, methods=["GET", "POST", "PUT", "DELETE"])