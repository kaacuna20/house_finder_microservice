import threading
from src.services.activity_log_service import ActivityLogService


class LoggingThread(threading.Thread):
    def __init__(self, log_data: dict):
        super().__init__()
        self.activity_log_service = ActivityLogService
        self.log_data = log_data
        
    def run(self):
        try:
            self.activity_log_service.create_activity_log(self.log_data)
        except Exception as e:
            print(f"Error logging activity: {e}")