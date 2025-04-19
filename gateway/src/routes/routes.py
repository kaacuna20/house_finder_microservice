from src.controllers.route_controller import RouteController
from flask import Blueprint


route_bp = Blueprint("route", __name__)
route_api = RouteController()

route_bp.add_url_rule("/", view_func=route_api.list, methods=["POST"])
route_bp.add_url_rule("/create", view_func=route_api.create, methods=["POST"])
route_bp.add_url_rule("/update/<string:param>", view_func=route_api.update, methods=["PUT"])
route_bp.add_url_rule("/delete/<string:param>", view_func=route_api.delete, methods=["DELETE"])