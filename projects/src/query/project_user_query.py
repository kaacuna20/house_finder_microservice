from src.models.project_model import ProjectUserQualification, Project
from src.database.db_conection import db


class ProjectUserQualificationQuery:
    
    def get_by_user(self, user: str):
        """
        Get all qualifications for a specific user.
        """
        project_user_qualifications = db.session.query(ProjectUserQualification).filter_by(user_ref=user).all()
        return [pu.to_dict() for pu in project_user_qualifications]
    
    def get_by_project(self, project_slug: str):
        """
        Get all qualifications for a specific project.
        """
        project_user_qualifications = db.session.query(ProjectUserQualification).filter_by(project_ref=project_slug).all()
        return [pu.to_dict() for pu in project_user_qualifications]
    
    def create(self, data):
        """
        Create a new project user qualification.
        """
        project_user_qualification = ProjectUserQualification(**data.dict())
        db.session.add(project_user_qualification)
        db.session.commit()
        
        self.add_avg_project(data.project_ref)
        db.session.refresh(project_user_qualification)
        
        return project_user_qualification.to_dict()
    
    def delete(self, id: int):
        """
        Delete a project user qualification by ID.
        """
        project_user_qualification = db.session.query(ProjectUserQualification).get(id)
        if project_user_qualification:
            db.session.delete(project_user_qualification)
            db.session.commit()
            return True
        return False
    
    def add_avg_project(self, project_slug: str):
        """
        Add the average qualification for a project.
        """
        
        project = db.session.query(Project).filter_by(slug=project_slug).first()
        if not project:
            return None
        
        qualifications = db.session.query(ProjectUserQualification).filter_by(project_ref=project_slug).all()
        if not qualifications:
            return None
        
        avg_qualification = sum([q.qualification for q in qualifications]) / len(qualifications)
        project.avg= avg_qualification
        db.session.commit()
        
        return True

