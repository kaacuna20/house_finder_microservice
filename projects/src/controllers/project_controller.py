from flask import request
from flask.views import MethodView
from src.services.project_service import ProjectService
from src.utils.serializers import CreateProject
from src.utils.http_response import http_response


class ProjectController(MethodView):
    
    def __init__(self):
        self.service = ProjectService()
        
    def list(self):
        projects = self.service.getAll()
        return http_response(projects.status_code, projects.message, projects.data, projects.error)
        
    def retrieve(self, param=None):
        project = self.service.getBySlug(param)
        return http_response(project.status_code, project.message, project.data, project.error)
    
    def create(self):
        data = CreateProject(**request.json)    
        project = self.service.create(data)
        return http_response(project.status_code, project.message, project.data, project.error)

        
    def update(self, id=None):
        data = CreateProject(**request.json)
        project = self.service.update(id, data)
        return http_response(project.data, project.status_code, project.message, project.error)
        
        
    def delete(self, id=None):
        project_deleted = self.service.delete(id)
        return http_response(project_deleted.data, project_deleted.status_code, project_deleted.message, project_deleted.error)
    
    def sync(self):
        data = self.service.sync()
        return http_response(data.status_code, data.message, data.data, data.error)
        
        