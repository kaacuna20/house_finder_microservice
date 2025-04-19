from abc import ABC, abstractmethod


class IAuthenticateService(ABC):
    @abstractmethod
    def authenticate(self, data) -> bool:
        """Authenticate a user with the given username and password."""
        pass
    
    @abstractmethod
    def generate_token(self, user_id: int) -> dict:
        """Generate a token for the authenticated user."""
        pass
    
    @abstractmethod
    def get_user_from_token(self, token) -> dict:
        """Retrieve user information from the token."""
        pass

    
    