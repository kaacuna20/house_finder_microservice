from flask.views import MethodView
from flask import request
from src.services.activity_log_service import ActivityLogService
from src.utils.serializers import CreateLog, GetItemLog
from src.utils.http_response import http_response


class ActivityLogController(MethodView):
    """Controller for managing activity logs."""

    def __init__(self):
        self.service = ActivityLogService()

    def list(self):
        """List activity logs."""
        item = GetItemLog(**request.json) if request.json else None
        limit = request.args.get("limit", 25)
        sort_by = request.args.get("sort_by", "create_at")

        logs = self.service.get_logs(item, int(limit), sort_by)
        return http_response(logs.status_code, logs.message, logs.data, logs.error)

    def retrieve(self):
        """Retrieve a specific activity log."""
        item = GetItemLog(**request.json)
        log = self.service.get_log(item)
        return http_response(log.status_code, log.message, log.data, log.error)

    def create(self):
        """Create a new activity log."""
        data = CreateLog(**request.json)
        log = self.service.create_activity_log(data)
        return http_response(log.status_code, log.message, log.data, log.error)
