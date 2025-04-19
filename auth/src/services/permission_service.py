from src.services.interfaces.IPermissionService import IPermisionService
from src.utils.serializers import CreatePermision
from src.query.permission_query import PermissionQuery
from src.utils.model_object import DataResponse
from http import HTTPStatus


class PermisionService(IPermisionService):
    
    def __init__(self):
        self.query = PermissionQuery()

    def get_permissions_by_role(self, role):
        response = DataResponse()
        try:
            permisions = self.query.get_by_role(role)
            if not permisions:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "No permissions found for the given role"
                return response
            response.data = permisions
            response.message = "Permissions fetched successfully"
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error fetching permissions by role"
            response.error = str(e.args)
            return response
        
    def get_permissions_by_reference(self, reference):
        response = DataResponse()
        try:
            permision = self.query.get_by_reference(reference)
            if not permision:
                response.data = None
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Permission not found"
                return response
            response.data = permision
            response.message = "Permission fetched successfully"
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error fetching permission by reference"
            response.error = str(e.args)
            return response
        
    def create(self, data: CreatePermision):
        response = DataResponse()
        try:
            permision = self.query.create(data)
            response.data = permision
            response.message = "Permission created successfully"
            response.status_code = HTTPStatus.CREATED
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating permission"
            response.error = str(e.args)
            return response
        
    def update(self, data: CreatePermision, pk: int):
        response = DataResponse()
        try:
            if not pk:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid ID provided"
                return response
            permision_update = self.query.update(pk, data)
            if not permision_update:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Permission not found"
                return response
            response.data = permision_update
            response.message = "Permission updated successfully"
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error updating permission"
            response.error = str(e.args)
            return response
                
    def delete(self, pk):
        response = DataResponse()
        try:
            if not pk:
                response.data = None
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Invalid ID provided"
                return response
            deleted = self.query.delete(pk)
            if not deleted:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Permission not found"
                return response
            response.message = "Permission deleted successfully"
            response.status_code = HTTPStatus.NO_CONTENT
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error deleting permission"
            response.error = str(e.args)
            return response