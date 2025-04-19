from sqlalchemy import String, Boolean, JSON, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from src.database.db_conection import db
from src.models.role_model import Role


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(Integer, primary_key=True, index=True)
    reference = db.Column(String(255), unique=True, index=True, nullable=False)
    name = db.Column(String(255), unique=True, index=True, nullable=False)
    service = db.Column(String(100), nullable=True)  # Service name
    module = db.Column(String(100), nullable=True)  # Module name
    actions = db.Column(JSON, nullable=True)  # JSON to store actions ['create', 'view', 'update', 'delete', ...]
    is_active = db.Column(Boolean, default=True)  # 1 for active, 0 for inactive
    role_reference = db.Column(String(255), ForeignKey("roles.reference"), nullable=False)
    
    role = relationship("Role", back_populates="permissions")
    
    __table_args__ = (
        UniqueConstraint('service', 'module','role_reference', name='uq_service_module_role_reference'),
    )    
    
    def to_dict(self):
        return {
            "id": self.id,
            "reference": self.reference,
            "name": self.name,
            "service": self.service,
            "actions": self.actions,
            "is_active": self.is_active,
            "role_reference": self.role_reference,
        }
        
    def module_actions(self):
        return {
            self.service: {self.module: self.actions},
        }