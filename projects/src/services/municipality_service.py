import logging
from src.services.interfaces.IMunicipalityService import IMunicipalityService
from src.utils.model_object import DataResponse
from src.utils.serializers import CreateMunicipality
from src.query.municipality_query import MunicipalityQuery
from http import HTTPStatus

logger = logging.getLogger(__name__)


class MunicipalityService(IMunicipalityService):
    def __init__(self):
        self.query = MunicipalityQuery()
        
    def getAll(self):
        response = DataResponse()
        try:
            municipalities = self.query.getAll()
            response.data = municipalities
            response.status_code = HTTPStatus.OK
            response.message = "Municipalities retrieved successfully"
            return response
        except Exception as e:
            logger.error(f"Error retrieving municipalities: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving municipalities"
            response.error = str(e.args)
            return response
        
    def getByCode(self, code):
        response = DataResponse()
        try:
            if not code:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Code is required"
                return response
            municipality = self.query.get_by_code(code)
            if not municipality:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Municipality not found"
                return response
            response.data = municipality
            response.status_code = HTTPStatus.OK
            response.message = "Municipality retrieved successfully"
            return response
        except Exception as e:
            logger.error(f"Error retrieving municipality by code {code}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving municipality"
            response.error = str(e.args)
            return response
        
    def create(self, data: CreateMunicipality):
        response = DataResponse()
        try:
            municipality = self.query.create(data)
            response.data = municipality
            response.status_code = HTTPStatus.CREATED
            response.message = "Municipality created successfully"
            return response
        except Exception as e:
            logger.error(f"Error creating municipality: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating municipality"
            response.error = str(e.args)
            return response
        
    def update(self, id: int, data: CreateMunicipality):
        response = DataResponse()
        try:
            municipality = self.query.update(id, data)
            if not municipality:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Municipality not found"
                return response
            response.data = municipality
            response.status_code = HTTPStatus.OK
            response.message = "Municipality updated successfully"
            return response
        except Exception as e:
            logger.error(f"Error updating municipality with ID {id}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error updating municipality"
            response.error = str(e.args)
            return response
        
    def delete(self, id: int):
        response = DataResponse()
        try:
            municipality = self.query.delete(id)
            if not municipality:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Municipality not found"
                return response
            response.status_code = HTTPStatus.OK
            response.message = "Municipality deleted successfully"
            return response
        except Exception as e:
            logger.error(f"Error deleting municipality with ID {id}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error deleting municipality"
            response.error = str(e.args)
            return response