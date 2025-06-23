import logging
from src.services.interfaces.IRoleService import IRoleService
from src.query.role_query import RoleQuery
from src.utils.serializers import CreateRole
from src.utils.model_object import DataResponse
from http import HTTPStatus

logger = logging.getLogger(__name__)

class RoleService(IRoleService):
    
    def __init__(self):
        self.query = RoleQuery()
    
    def GetAll(self):
        response = DataResponse()
        try:
            roles = self.query.getAll()
            response.data = roles
            response.message = "Roles fetched successfully"
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            logger.error(f"Error fetching roles: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error fetching roles"
            response.error = str(e.args)
            return response
    
    def GetById(self, id):
        response = DataResponse()
        try:
            role = self.query.get_by_id(id)
            if not role:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Role not found"
                return response
            response.data = role
            response.message = "Role fetched successfully"
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            logger.error(f"Error fetching role with ID {id}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = f"Error fetching role with ID {id}"
            response.error = str(e.args)
            return response
        
    def create(self, data: CreateRole):
        response = DataResponse()
        try:
            new_role = self.query.create(data)
            response.data = new_role
            response.message = "Role created successfully"
            response.status_code = HTTPStatus.CREATED
            return response
        except Exception as e:
            logger.error(f"Error creating role: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating role"
            response.error = str(e.args)
            return response
    
    def update(self, data: CreateRole, pk):
        response = DataResponse()
        try:
            if not pk:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid ID provided"
                return response
            updated_role = self.query.update(data, pk)
            if not updated_role:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Role not found"
                return response
            response.data = updated_role
            response.message = "Role updated successfully"
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            logger.error(f"Error updating role with ID {pk}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = f"Error updating role with ID {pk}"
            response.error = str(e.args)
            return response
    
    def delete(self, pk):
        response = DataResponse()
        try:
            deleted_role = self.query.delete(pk)
            if not deleted_role:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Role not found"
                return response
            response.message = "Role deleted successfully"
            response.status_code = HTTPStatus.NO_CONTENT
            return response
        except Exception as e:
            logger.error(f"Error deleting role with ID {pk}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = f"Error deleting role with ID {pk}"
            response.error = str(e.args)
            return response