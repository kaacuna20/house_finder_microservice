import logging
from flask_jwt_extended import create_access_token
from src.services.interfaces.IAuthenticateService import IAuthenticateService
from src.utils.serializers import AuthUser, Token
from flask_jwt_extended import decode_token
from src.utils.model_object import DataResponse
from src.query.authenticate_query import AuthenticateQuery
from http import HTTPStatus

logger = logging.getLogger(__name__)

class AuthenticateService(IAuthenticateService):
    
    def __init__(self):
        self.authenticate_query = AuthenticateQuery()
    
    def authenticate(self, login_request: AuthUser):
        """Authenticate a user with the given email and password."""
        response = DataResponse()
        try:
            user = self.authenticate_query.get_user_by_email(login_request.email)
            if user and user.verify_password(login_request.password):
                token = self.generate_token(user.email)
                response.status_code = HTTPStatus.OK
                response.message = "User authenticated successfully."
                response.data = token
            else:
                response.status_code = HTTPStatus.UNAUTHORIZED
                response.message = "Invalid credentials."
                response.error = "Invalid email or password."
            return response
        except Exception as e:
            logger.error(f"Authentication error: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Authentication failed."
            response.error = str(e)
            return response

    def generate_token(self, user):
        """Generate a token for the authenticated user."""
        token = create_access_token(identity=user)
        logger.info(f"Token generated for user: {user}")
        return {"access_token": token, "token_type": "Bearer"}



    def get_user_from_token(self, token: Token) -> dict:
        """Retrieve user information from the token."""
        response = DataResponse()
        try:
            decoded_token = decode_token(token.access_token)
            user_decoded = decoded_token.get("sub")
            logger.info(f"Decoded token: {decoded_token}")
            if not user_decoded:
                response.status_code = HTTPStatus.UNAUTHORIZED
                response.message = "Invalid token."
                response.error = "Token does not contain user information."
                return response

            # Busca el usuario en la base de datos
            user = self.authenticate_query.get_user_by_email(user_decoded)

            if not user:
                response.status_code = HTTPStatus.UNAUTHORIZED
                response.message = "Invalid token."
                response.error = "User not found."
                return response
            
            response.status_code = HTTPStatus.OK
            response.message = "User retrieved successfully."
            response.data = user.to_dict()
            return response

        except Exception as e:
            logger.error(f"Error retrieving user from token: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Failed to retrieve user from token."
            response.error = str(e)
            return response
