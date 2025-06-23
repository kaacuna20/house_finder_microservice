import logging
from src.services.interfaces.IProjectUserQualification import IProjectUserQualification
from src.query.project_user_query import ProjectUserQualificationQuery
from src.integrations.auth_api import AuthApi   
from src.utils.serializers import CreateProjectUserQualification
from src.utils.model_object import DataResponse
from http import HTTPStatus

logger = logging.getLogger(__name__)

class ProjectUserQualificationService(IProjectUserQualification):
    
    def __init__(self):
        self.query = ProjectUserQualificationQuery()
        self.auth_api = AuthApi()
        
    def get_qualifications_by_user(self, user: str):
        response = DataResponse()
        try:
            logger.info(f"Fetching qualifications for user: {user}")
            if not user:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "User email is required."
                return response
            qualifications = self.query.get_by_user(user)
            logger.info(f"Qualifications found: {qualifications}")
            if not qualifications:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "No qualifications found for this user."
                return response
            
            response.data = qualifications
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            logger.error(f"Error fetching qualifications for user {user}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = str(e.args)
            return response
        
    def get_qualifications_by_project(self, project_slug: str):
        response = DataResponse()
        try:
            logger.info(f"Fetching qualifications for project: {project_slug}")
            if not project_slug:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Project slug is required."
                return response
            
            qualifications = self.query.get_by_project(project_slug)
            logger.info(f"Qualifications found: {qualifications}")
            if not qualifications:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "No qualifications found for this project."
                return response
            
            response.data = qualifications
            response.status_code = HTTPStatus.OK
            return response
        except Exception as e:
            logger.error(f"Error fetching qualifications for project {project_slug}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = str(e.args)
            return response
        
    def create(self, request, data):
        response = DataResponse()
        
        try:
            user_data = self.auth_api.get_user(request.headers.get("Authorization"))
            user = user_data.get('data')['email'] if user_data else None
            created_data = CreateProjectUserQualification(
                project_ref=data.get('project'),
                user_ref=user,
                qualification=data.get('qualification'),    
            )
            qualification = self.query.create(created_data)
            response.data = qualification
            response.status_code = HTTPStatus.CREATED
            response.message = "Qualification created successfully."
            return response
        except Exception as e:
            logger.error(f"Error creating qualification: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating qualification: "
            response.data = str(e.args)
            return response
        
    def delete(self, id: int):
        response = DataResponse()
        try:
            if not id:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Qualification ID is required."
                return response
            
            deleted = self.query.delete(id)
            if not deleted:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Qualification not found."
                return response
            
            response.status_code = HTTPStatus.OK
            response.message = "Qualification deleted successfully."
            return response
        except Exception as e:
            logger.error(f"Error deleting qualification with ID {id}: {str(e)}")
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error deleting qualification"
            response.data = str(e)
            return response