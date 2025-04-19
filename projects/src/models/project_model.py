from src.database.db_conection import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, CheckConstraint, ForeignKey,UniqueConstraint, DECIMAL
from sqlalchemy.orm import relationship
from slugify import slugify


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(Integer, primary_key=True, index=True)
    name = db.Column(String(255), nullable=False)
    logo = db.Column(String(500), nullable=True)
    description = db.Column(Text, nullable=True)
    location = db.Column(String(255), nullable=True)
    municipality_divipola = db.Column(String(100), ForeignKey("municipalities.divipola_code"), nullable=False)
    company_nit = db.Column(String(100), ForeignKey("companies.nit"), nullable=False)
    address = db.Column(String(255), nullable=True)
    contact = db.Column(String(255), nullable=True)
    area = db.Column(Float, nullable=True)
    price = db.Column(Integer, nullable=True)
    type = db.Column(String(100), nullable=True)
    img_url = db.Column(String(500), nullable=True)
    url_website = db.Column(String(255), nullable=True)
    slug = db.Column(String(255), nullable=False, unique=True, index=True)
    latitude = db.Column(Float, nullable=True)
    longitude = db.Column(Float, nullable=True)
    avg = db.Column(DECIMAL(10, 2), nullable=True)  # Average rating
    created_at = db.Column(DateTime, nullable=True)
    updated_at = db.Column(DateTime, nullable=True)
    
    municipality = relationship("Municipality", back_populates="project")
    company = relationship("Company", back_populates="project")
    project_user_qualifications = db.relationship("ProjectUserQualification", back_populates="project")

    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.slug = slugify(self.name)  # Generate slug on object creation
        super(Project, self).__init__(*args, **kwargs)  # Call parent constructor

    def save(self, *args, **kwargs):
        is_new = self.id is None
        if is_new:
            self.created_at = datetime.now()

        self.updated_at = datetime.now()
        self.slug = slugify(self.name.lower())
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "logo": self.logo,
            "description": self.description,
            "location": self.location,
            "municipality": self.municipality.to_dict() if self.municipality else None,
            "company": self.company.to_dict() if self.company else None,
            "address": self.address,
            "contact": self.contact,
            "area": self.area,
            "price": self.price,
            "type": self.type,
            "img_url": self.img_url,
            "url_website": self.url_website,
            "slug": self.slug,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "avg": self.avg
        }
    
    def __repr__(self):
        return f'<Project {self.name}>'

    __table_args__ = (
        CheckConstraint('price >= :0', name='min_integer_check'),
        CheckConstraint('area >= :0', name='min_float_check'),
    )
    
    
class ProjectUserQualification(db.Model):
    __tablename__ = "project_users_qualifications"
    id = db.Column(Integer, primary_key=True, index=True)
    user_ref = db.Column(String(255), nullable=False)
    project_ref = db.Column(String(255), ForeignKey('projects.slug'), nullable=False)
    qualification = db.Column(Float, nullable=False)
    
    project = db.relationship("Project", back_populates="project_user_qualifications")
    
    __table_args__ = (
        CheckConstraint('qualification >= 0', name='min_float_check'),
        UniqueConstraint('user_ref', 'project_ref', name='uq_user_project_qualification')
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user_ref,
            "project": self.project.to_dict() if self.project else [],
            "qualification": self.qualification,
        }    
    
    def __repr__(self):
        return f'<ProjectUser {self.user_ref} in {self.project_ref}>'