from abc import ABC, abstractmethod


class IRouteTableService(ABC):
    
    @abstractmethod
    def get_route_table(self):
        """Get the route table."""
        pass

    @abstractmethod
    def add_route(self, route):
        """Add a route to the route table."""
        pass

    @abstractmethod
    def delete_route(self, route_id):
        """Delete a route from the route table."""
        pass

    @abstractmethod
    def update_route(self, route_id, new_route):
        """Update a route in the route table."""
        pass