from datetime import datetime
from pymongo import DESCENDING
from src.database.db_conection import client
from src.utils.settings import Settings

config = Settings.get_config()


class ActivityLog:
    def __init__(self, table_name="logs"):
        self.db = client[config.DB_NAME]
        self.__collection = self.db[table_name]
    
    def get_collection(self, table_name):
        """Get a collection from the MongoDB client."""
        return client[table_name]
    
    def insert_log(self, log_entry):
        """Insert a log entry into the activity log collection."""
        
        log_entry["created_at"] = datetime.now()
        log_entry["updated_at"] = datetime.now()
        log = self.__collection.insert_one(log_entry)
        log_id = log.inserted_id
        log_entry["_id"] = str(log_id)
        return log_entry
        
    
    def get_logs(self, filter=None, limit=25, sort_by="create_at", sort_order=DESCENDING):
        """Retrieve logs from the activity log collection."""
        query = filter or {}
        logs_cursor = self.__collection.find(query).sort(sort_by, sort_order).limit(limit)
        logs = []

        for log in logs_cursor:
            log["_id"] = str(log["_id"])  # Convertir ObjectId a str
            logs.append(log)

        return logs
    
    def count_logs(self, filter=None):
        """Count the number of logs in the activity log collection."""
        if filter:
            return self.__collection.count_documents(filter)
        return self.__collection.count_documents({})
    
    def get_log_by_item(self, item:dict):
        """Retrieve a log entry by its item."""
        log = self.__collection.find_one(item)
        log["_id"] = str(log["_id"])
        return log
    
    def get_log_by_path(self, path):
        """Retrieve a log entry by its path."""
        log =  self.__collection.find_one({"path": path})
        log["_id"] = str(log["_id"])  # Convertir ObjectId a str
        return log
    
    def get_log_by_service_id(self, service_id):
        """Retrieve a service info by its service id."""
        log= self.__collection.find_one({"service_id": service_id})
        log["_id"] = str(log["_id"])  # Convertir ObjectId a str
        return log