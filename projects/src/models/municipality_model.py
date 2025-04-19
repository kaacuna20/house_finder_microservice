from src.database.db_conection import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Municipality(db.Model):
    __tablename__ = "municipalities"
    id = db.Column(Integer, primary_key=True, index=True)
    divipola_code = db.Column(String, unique=True, index=True, nullable=False)
    name = db.Column(String, unique=True, index=True, nullable=False)
    created_at = db.Column(DateTime, nullable=True)
    updated_at = db.Column(DateTime, nullable=True)
    
    project = relationship("Project", back_populates="municipality")

    def save(self, *args, **kwargs):
        is_new = self.id is None
        if is_new:
            self.created_at = datetime.now()
        else:
            self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        
    def to_dict(self):
        return {
            "id": self.id,
            "divipola_code": self.divipola_code,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self):
        return f'<City {self.name}>'