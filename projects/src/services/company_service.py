from src.services.interfaces.ICompanyService import ICompanyService
from src.utils.model_object import DataResponse
from src.utils.serializers import CreateCompany
from src.query.company_query import CompanyQuery
from http import HTTPStatus


class CompanyService(ICompanyService):
    
    def __init__(self):
        self.query = CompanyQuery()
    
    def getAll(self):
        response = DataResponse()
        try:
            companies = self.query.getAll()
            response.data = companies
            response.status_code = HTTPStatus.OK
            response.message = "Companies retrieved successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving companies"
            response.error = str(e)
            return response
        
    def getByNit(self, nit):
        response = DataResponse()
        try:
            if not nit:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "NIT is required"
                return response
            company = self.query.get_by_nit(nit)
            if not company:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Company not found"
                return response
            response.data = company
            response.status_code = HTTPStatus.OK
            response.message = "Company retrieved successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error retrieving company"
            response.error = str(e)
            return response
            
    def create(self, data: CreateCompany):
        response = DataResponse()
        try:
            company = self.query.create(data)
            response.data = company
            response.status_code = HTTPStatus.CREATED
            response.message = "Company created successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating company"
            response.error = str(e)
            return response
        
    def update(self, id: int, data: CreateCompany):
        response = DataResponse()
        try:
            if not id:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "ID is required"
                return response
            company = self.query.update(id, data)
            if not company:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Company not found"
                return response
            response.data = company
            response.status_code = HTTPStatus.OK
            response.message = "Company updated successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error updating company"
            response.error = str(e)
            return response
    def delete(self, id):
        response = DataResponse()
        try:
            if not id:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "ID is required"
                return response
            company = self.query.delete(id)
            if not company:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Company not found"
                return response
            response.data = company
            response.status_code = HTTPStatus.OK
            response.message = "Company deleted successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error deleting company"
            response.error = str(e)
            return response