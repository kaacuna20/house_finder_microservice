from flask import Blueprint
from src.controllers.sync_controller import SyncController


sync_bp = Blueprint("sync", __name__)
sync_api = SyncController()

sync_bp.add_url_rule('/house-projects', view_func=sync_api.sync, methods=['POST'])