from flask import Blueprint
from src.controllers.activity_log_controller import ActivityLogController


log_bp = Blueprint("activity_log", __name__)

log_api = ActivityLogController()
log_bp.add_url_rule("/", view_func=log_api.list, methods=["POST"])
log_bp.add_url_rule("/log", view_func=log_api.retrieve, methods=["POST"])
log_bp.add_url_rule("/insert-log", view_func=log_api.create, methods=["POST"])


