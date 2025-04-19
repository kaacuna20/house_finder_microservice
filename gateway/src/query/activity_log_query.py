from src.models.activity_log_model import ActivityLog


class ActivityLogQuery:
    
    def __init__(self):
        self.__activity_log = ActivityLog()
        
    
    def get_logs(self, filter, limit: int = 25, sort_by: str = "created_at", sort_order: int = -1) -> list:
        """Retrieve all activity logs."""
        return self.__activity_log.get_logs(filter, limit, sort_by, sort_order)
    
    def create_activity_log(self, data: dict) -> dict:
        """Create a new activity log entry."""
        return self.__activity_log.insert_log(data)
    
    def get_log(self, data: dict) -> list:
        """Retrieve activity logs for a specific item."""
        return self.__activity_log.get_log_by_item(data)