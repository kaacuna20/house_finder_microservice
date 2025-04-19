from src.database.db_conection import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(Integer, primary_key=True, index=True)
    nit = db.Column(String, unique=True, index=True, nullable=False)
    name = db.Column(String, unique=True, nullable=False)
    address = db.Column(String, nullable=True)
    contact = db.Column(String, nullable=True)
    created_at = db.Column(DateTime, nullable=True)
    updated_at = db.Column(DateTime, nullable=True)
    
    project = relationship("Project", back_populates="company")
    
    def save(self, *args, **kwargs):
        is_new = self.id is None
        if is_new:
            self.created_at = datetime.now()
    
        self.updated_at = datetime.now()
        
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        
    def to_dict(self):
        return {
            "id": self.id,
            "nit": self.nit,
            "name": self.name,
            "address": self.address,
            "contact": self.contact,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        
    def __repr__(self):
        return f'<Company {self.name}>'
    


