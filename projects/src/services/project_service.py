from src.services.interfaces.IProjectService import IProjectService
from src.integrations.scraping_api import ScrapingAPI
from src.utils.serializers import CreateProject
from src.utils.model_object import DataResponse
from src.query.project_query import ProjectQuery 
from http import HTTPStatus

class ProjectService(IProjectService):
    
    def __init__(self):
        self.query = ProjectQuery()
        self.scraping_api = ScrapingAPI()
    
    def getAll(self):
        response = DataResponse()
        try:
            projects = self.query.getAll()
            response.data = projects
            response.status_code = HTTPStatus.OK
            response.message = "Projects fetched successfully"
            return response 
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error fetching projects"
            response.error = str(e.args)
            return response    

    def getBySlug(self, slug: str):
        response = DataResponse()
        try:
            if not slug:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "Slug is required"
                return response
            
            project = self.query.get_by_slug(slug)
            if not project:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Project not found"
                return response
            response.data = project
            response.status_code = HTTPStatus.OK
            response.message = "Project fetched successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR    
            response.message = "Error fetching project"
            response.error = str(e.args)
            return response
        
    def create(self, data: CreateProject):
        response = DataResponse()
        try:
            data.logo = str(data.logo) if data.logo else None
            data.img_url = str(data.img_url) if data.img_url else None
            data.url_website = str(data.url_website) if data.url_website else None
            project = self.query.create(data)
            response.data = project
            response.status_code = HTTPStatus.CREATED
            response.message = "Project created successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error creating project"
            response.error = str(e.args)
            return response
        
    def update(self, id: int, data: CreateProject):
        response = DataResponse()
        try:
            data.logo = str(data.logo) if data.logo else None
            data.img_url = str(data.img_url) if data.img_url else None
            data.url_website = str(data.url_website) if data.url_website else None
            project = self.query.update(id, data)
            if not project:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Project not found"
                return response
            response.data = project
            response.status_code = HTTPStatus.OK
            response.message = "Project updated successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error updating project"
            response.error = str(e.args)
            return response
        
    def delete(self, id):
        response = DataResponse()
        try:
            if not id:
                response.status_code = HTTPStatus.BAD_REQUEST
                response.message = "ID is required"
                return response
            project_deleted = self.query.delete(id)
            if not project_deleted:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "Project not found"
                return response
            response.status_code = HTTPStatus.NO_CONTENT
            response.message = "Project deleted successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error deleting project"
            response.error = str(e.args)
            return response
        
    def sync(self):
        response = DataResponse()
        try:
            data_request = self.scraping_api.get_data()
            if not data_request:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "No data found"
                return response
            
            projects = data_request.get("data")['projects'] if data_request.get("data") else []
            if not projects:
                response.status_code = HTTPStatus.NOT_FOUND
                response.message = "No projects found"
                return response
            
            for project in projects:
                data = CreateProject(
                    name=project.get("name"),
                    logo=project.get("logo"),
                    description=project.get("description"),
                    location=project.get("location"),
                    municipality_divipola=str(project.get("divipola")),
                    company_nit=project.get("nit"),
                    address=project.get("address"),
                    contact=project.get("contact"),
                    area=project.get("area"),
                    price=project.get("price"),
                    type=project.get("type"),
                    img_url=project.get("img_url"),
                    url_website=project.get("url_website"),
                    latitude=project.get("latitude"),
                    longitude=project.get("longitude")
                )
                data.logo = str(data.logo) if data.logo else None
                data.img_url = str(data.img_url) if data.img_url else None
                data.url_website = str(data.url_website) if data.url_website else None
                self.query.create_or_update(data)
                
            
            response.data = {"projects_syncs": data_request.get("data")['count']}
            response.status_code = HTTPStatus.OK
            response.message = "Projects synced successfully"
            return response
        except Exception as e:
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response.message = "Error syncing projects"
            response.error = str(e)
            return response

    