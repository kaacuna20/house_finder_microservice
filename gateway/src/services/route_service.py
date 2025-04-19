from src.services.interfaces.IRouteTableService import IRouteTableService
from src.query.routes_query import RouteQuery
from src.utils.serializers import CreateRoute, GetItemRoute
from src.utils.model_object import DataResponse
from http import HTTPStatus


class RouteTableService(IRouteTableService):
    """Service class for managing routes in the route table."""

    def __init__(self):
        """Initialize the route table service."""
        self.query = RouteQuery()

    def get_route_table(self, filter: GetItemRoute=None, limit=25, sort_by="create_at") -> list:
        """Retrieve all routes from the route table."""
        response = DataResponse()
        try:
            if filter:
                filter_format = GetItemRoute(**filter.to_dict()).to_dict()
            else:
                filter_format = {}
            route = self.query.get_routes(filter_format, limit, sort_by)
            response.data = route
            response.status_code = HTTPStatus.OK
            response.message = "Routes retrieved successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving routes."
            response.error = str(e)
            return response

    def add_route(self, data: CreateRoute) -> dict:
        """Create a new route entry."""
        response = DataResponse()
        try:
            data = CreateRoute(**data.to_dict())
            route = self.query.create_route(data.to_dict())
            response.data = route
            response.status_code = HTTPStatus.CREATED
            response.message = "Route created successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating route."
            response.error = str(e)
            return response
    
    def update_route(self, route_id, new_route):
        """Update a route in the route table."""
        response = DataResponse()
        try:
            route = self.query.update_route(route_id, new_route)
            response.data = route
            response.status_code = HTTPStatus.OK
            response.message = "Route updated successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error updating route."
            response.error = str(e)
            return response
    
    def delete_route(self, route_id):
        """Delete a route from the route table."""
        response = DataResponse()
        try:
            route = self.query.delete_route(route_id)
            response.data = route
            response.status_code = HTTPStatus.OK
            response.message = "Route deleted successfully."
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error deleting route."
            response.error = str(e)
            return response