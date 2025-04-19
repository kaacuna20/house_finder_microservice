from src.services.route_service import RouteTableService
from flask import request
from src.utils.serializers import CreateRoute, GetItemRoute
from src.utils.http_response import http_response



class RouteController:
    """Controller for managing routes."""

    def __init__(self):
        self.service = RouteTableService()

    def list(self):
        """List routes."""
        item = GetItemRoute(**request.json) if request.json else None
        limit = request.args.get("limit", 25)
        sort_by = request.args.get("sort_by", "create_at")
        routes = self.service.get_route_table(item, int(limit), sort_by)
        return http_response(routes.status_code, routes.message, routes.data, routes.error)

    def create(self):
        """Create a new route."""
        data = CreateRoute(**request.json)
        route = self.service.add_route(data)
        return http_response(route.status_code, route.message, route.data, route.error)
        
        
    def update(self, param=None):
        """Update a route."""
        new_route = request.json
        updated_route = self.service.update_route(param, new_route)
        return http_response(updated_route.status_code, updated_route.message, updated_route.data, updated_route.error)
        
    def delete(self, param=None):
        """Delete a route."""
        deleted = self.service.delete_route(param)
        return http_response(deleted.status_code, deleted.message, deleted.data, deleted.error)




