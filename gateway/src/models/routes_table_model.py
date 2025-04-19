from pymongo import DESCENDING
from bson.objectid import ObjectId
from src.database.db_conection import client
from src.utils.settings import Settings

config = Settings.get_config()


class RoutesTable:
    """RoutesTable class to manage the routes collection in MongoDB."""
    def __init__(self, table_name="routes"):
        self.db = client[config.DB_NAME]
        self.__collection = self.db[table_name]
    
    def get_collection(self, table_name):
        """Get a collection from the MongoDB client."""
        return client[table_name]
    
    def insert_route(self, route_entry):
        """Insert a data route entry into the routes table collection."""
        route = self.__collection.insert_one(route_entry)
        route_id = route.inserted_id
        route_entry["_id"] = str(route_id)
        return route_entry
    
    def get_routes(self, filter=None, limit=25, sort_by="create_at", sort_order=DESCENDING):
        """Retrieve logs from the routes table collection."""
        query = filter or {}
        routes_cursor = self.__collection.find(query).sort(sort_by, sort_order).limit(limit)
        routes = []

        for route in routes_cursor:
            route["_id"] = str(route["_id"])  # Convertir ObjectId a str
            routes.append(route)

        return routes
    
    def update_route(self, route_id, new_route):
        """Update a route in the routes table collection."""
        object_id = ObjectId(route_id)
        result = self.__collection.update_one({"_id": object_id}, {"$set": new_route})
        return result.modified_count > 0
    
    def count_routes(self, filter=None):
        """Count the number of routes in the routes table collection."""
        if filter:
            return self.__collection.count_documents(filter)
        return self.__collection.count_documents({})
    
    def delete_route(self, route_id):
        """Delete a route from the routes table collection."""
        object_id = ObjectId(route_id)
        result = self.__collection.delete_one({"_id": object_id})
        return result.deleted_count > 0 
    