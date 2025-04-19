from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from src.database.db_conection import db
from src.models.role_model import Role
from src.utils.settings import Settings


settings = Settings.get_config()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True, index=True)
    email = db.Column(String(255), unique=True, nullable=False)
    password = db.Column(String, nullable=False)
    is_active = db.Column(Boolean, default=True)  # 1 for active, 0 for inactive
    is_super_user = db.Column(Integer, default=0)  # 1 for superuser, 0 for regular user
    role_reference = db.Column(String(255), ForeignKey("roles.reference"), nullable=False)
    created_at = db.Column(DateTime, nullable=False)
    updated_at = db.Column(DateTime, nullable=False)
    
    role = db.relationship("Role", back_populates="users")
    
    def save(self, *args, **kwargs):
        is_new = self.id is None
        if is_new:
            self.created_at = datetime.now()

        self.updated_at = datetime.now()
        self.password = generate_password_hash(
            self.password, method=settings.HASH_METHOD, salt_length=settings.HASH_SALT_LENGTH
        )
        
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        
    def verify_password(self, password):
        return check_password_hash(self.password, password)
     

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "is_super_user": self.is_super_user,
            "role": self.role.to_dict() if self.role else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }