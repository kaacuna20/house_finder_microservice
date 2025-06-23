
import logging
from http import HTTPStatus
from src.query.user_query import UserQuery
from src.services.interfaces.IUserService import IUserService
from src.utils.serializers import CreateUser, UpdateUser
from src.utils.model_object import DataResponse

logger = logging.getLogger(__name__)

class UserService(IUserService):
    
    def __init__(self):
        self.query = UserQuery()
        
    def GetAll(self):
        response = DataResponse()
        try:
            users = self.query.get_all()
            response.data = users
            response.message = "Users fetched successfully"
            response.status_code = HTTPStatus.OK
            return response
        
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error fetching users"
            response.error = str(e.args)
            return response
    
    def GetById(self, id):
        response = DataResponse()
        try:
            if not id:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid ID provided"
                return response
            
            user = self.query.get_by_id(id)
            if not user:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "User not found"
                return response
            
            response.data = user
            response.message = "User fetched successfully"
            response.status_code = HTTPStatus.OK
            return response

        except Exception as e:
            logger.error(f"Error fetching user with ID {id}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = f"Error fetching user with ID {id}"
            response.error = str(e.args)
            return response
    
    def create(self, data: CreateUser):
        response = DataResponse()
        try:
            new_user = self.query.create(data)
            response.data = new_user
            response.message = "User created successfully"
            response.status_code = HTTPStatus.CREATED
            return response   
            
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating user"
            response.error = str(e.args)
            return response
    
    def update(self, data: UpdateUser, pk: int):
        response = DataResponse()
        try:
            if not pk:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid ID provided"
                return response
            
            user_updated = self.query.update(pk, data.to_dict())
            if not user_updated:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "User not found"
                return response
            response.data = user_updated
            response.message = "User updated successfully"
            response.status_code = HTTPStatus.OK
            return response
        
        except Exception as e:
            logger.error(f"Error updating user with ID {pk}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = f"Error updating user with ID {pk}"
            response.error = str(e.args)
            return response
            
    def delete(self, pk):
        response = DataResponse()
        try:
            if not pk:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid ID provided"
                return response
            
            deleted_user = self.query.get_by_id(pk) #self.query.delete(pk)
            if not deleted_user:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "User not found"
                return response
            
            self.query.delete(pk)
            response.message = "User deleted successfully"
            response.status_code = HTTPStatus.NO_CONTENT
            return response
        
        except Exception as e:
            logger.error(f"Error deleting user with ID {pk}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = f"Error deleting user with ID {pk}"
            response.error = str(e.args)
            return response
        
    
