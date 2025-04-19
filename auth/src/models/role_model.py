from sqlalchemy import String, Boolean, BigInteger, Text, Integer
from sqlalchemy.orm import relationship
from src.database.db_conection import db


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(Integer, primary_key=True, index=True)
    reference = db.Column(String(255), unique=True, index=True, nullable=False)
    name = db.Column(String(255), unique=True, index=True, nullable=False)
    description = db.Column(Text, nullable=True)
    is_active = db.Column(Boolean, default=True)  # 1 for active, 0 for inactive
    
    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", back_populates="role")
    
    def to_dict(self):
        return {
            "id": self.id,
            "reference": self.reference,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active,
            "permissions": [permission.module_actions() for permission in self.permissions] if self.permissions else [],
        }