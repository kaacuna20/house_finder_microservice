from src.services.interfaces.IActivityLogService import IActivityLogService
from src.query.activity_log_query import ActivityLogQuery
from src.utils.serializers import CreateLog, GetItemLog
from src.utils.model_object import DataResponse
from http import HTTPStatus


class ActivityLogService(IActivityLogService):
    """Service class for managing activity logs."""

    def __init__(self):
        """Initialize the activity log service."""
        self.query = ActivityLogQuery()

    def get_logs(self, filter: GetItemLog=None, limit=25, sort_by="created_at", sort_order=-1) -> list:
        """Retrieve all activity logs."""
        response = DataResponse()
        try:
            if filter:
                filter_format = GetItemLog(**filter.to_dict()).to_dict()
            else:
                filter_format = {}
            log =  self.query.get_logs(filter_format, limit, sort_by, sort_order)
            response.data = log
            response.status_code = HTTPStatus.OK
            response.message = "Logs retrieved successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving logs."
            response.error = str(e)
            return response
        
    def create_activity_log(self, data: CreateLog) -> dict:
        """Create a new activity log entry."""
        response = DataResponse()
        try:
            data = CreateLog(**data.to_dict())
            log = self.query.create_activity_log(data.to_dict())
            response.data = log
            response.status_code = HTTPStatus.CREATED
            response.message = "Log created successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating log."
            response.error = str(e)
            return response

    def get_log(self, data: GetItemLog) -> list:
        """Retrieve activity logs for a specific item."""
        response = DataResponse()
        try:
            data = GetItemLog(**data.to_dict())
            if not data:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid data provided."
                return response
            log = self.query.get_log(data.to_dict())
            response.data = log
            response.status_code = HTTPStatus.OK
            response.message = "Log retrieved successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving log."
            response.error = str(e)
            return response