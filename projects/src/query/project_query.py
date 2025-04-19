from sqlalchemy import and_, or_, not_
from src.database.db_conection import db
from src.models.project_model import Project


class ProjectQuery:
    
    def getAll(self):
        projects = db.session.query(Project).all()
        return [p.to_dict() for p in projects]
    
    def get_by_slug(self, slug: str):
        project = db.session.query(Project).filter(Project.slug == slug).first()
        if project:
            return project.to_dict()
        return None
    
    def create(self, data):
        project = Project(**data.dict())
        project.save()
        return project.to_dict()
    
    def update(self, id: int, data):
        project = db.session.query(Project).filter(Project.id == id).first()
        for key, value in data.dict(exclude_unset=True).items():
            setattr(project, key, value)
        db.session.commit()
        db.session.refresh(project)
        return project.to_dict()
    
    def delete(self, id: int):
        project = db.session.query(Project).filter(Project.id == id).first()
        if project:
            db.session.delete(project)
            db.session.commit()
            return True
        return False
    
    def create_or_update(self, data):

        project = db.session.query(Project).filter(
            and_(
                Project.name.like(data.name),
                Project.municipality_divipola.like(data.municipality_divipola),
                Project.company_nit.like(data.company_nit),
                Project.url_website.like(data.url_website),
            )
        ).first()
        
        if project:
            project.name = data.name
            project.logo = data.logo
            project.location = data.location
            project.municipality_divipola = data.municipality_divipola
            project.company_nit = data.company_nit
            project.address = data.address
            project.contact = data.contact
            project.area = data.area
            project.price = data.price
            project.type = data.type
            project.img_url = data.img_url
            project.description = data.description
            project.url_website = data.url_website
            project.latitude = data.latitude
            project.longitude = data.longitude
            project.save()
            return project.to_dict()
        else:
            new_project = Project(**data.dict())
            new_project.save()
            return new_project.to_dict()

