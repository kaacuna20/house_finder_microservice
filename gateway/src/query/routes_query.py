from src.models.routes_table_model import RoutesTable


class RouteQuery:
    
    def __init__(self):
        self.__routes_table = RoutesTable()
        
    def get_routes(self, filter, limit: int = 25, sort_by: str = "created_at", sort_order: int = -1) -> list:
        return self.__routes_table.get_routes(filter, limit, sort_by, sort_order)
    
    def create_route(self, data: dict) -> dict:
        return self.__routes_table.insert_route(data)
    
    def update_route(self, route_id, new_route):
        return self.__routes_table.update_route(route_id, new_route)
    
    def delete_route(self, route_id):
        return self.__routes_table.delete_route(route_id)