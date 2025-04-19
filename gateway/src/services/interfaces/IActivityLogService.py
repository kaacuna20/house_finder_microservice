from abc import ABC, abstractmethod


class IActivityLogService(ABC):
    
    @abstractmethod
    def get_logs(self, filter, limit, sort_by) -> list:
        """Retrieve all activity logs."""
        pass
    
    @abstractmethod
    def create_activity_log(self, data) -> dict:
        """Create a new activity log entry."""
        pass

    @abstractmethod
    def get_log(self, data) -> list:
        """Retrieve activity logs for a specific item."""
        pass
