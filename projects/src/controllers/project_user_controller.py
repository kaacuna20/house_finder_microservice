from flask import request
from flask.views import MethodView
from src.services.project_user_service import ProjectUserQualificationService
from src.utils.serializers import CreateProjectUserQualification
from src.utils.http_response import http_response


class ProjectUserQualificationController(MethodView):
    
    def __init__(self):
        self.service = ProjectUserQualificationService()
        
    def list(self):
        """
        List project user qualifications.
        """
        if request.args.get('project'):
            qualifications = self.service.get_qualifications_by_project(request.args.get('project'))
        else:
            qualifications = self.service.get_qualifications_by_user(request.args.get('user'))
        return http_response(qualifications.status_code, qualifications.message, qualifications.data, qualifications.error)  
    
    def create(self):
        """
        Create a new project user qualification.
        """
        data = request.get_json()
        qualification = self.service.create(request, data)
        return http_response(qualification.data, qualification.status_code, qualification.message, qualification.error)
    
    def delete(self, id=None):
        """
        Delete a project user qualification.
        """
        qualification_deleted = self.service.delete(id)
        return http_response(qualification_deleted.data, qualification_deleted.status_code, qualification_deleted.message, qualification_deleted.error)