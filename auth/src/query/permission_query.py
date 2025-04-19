from src.database.db_conection import db
from src.models.permission_model import Permission


class PermissionQuery:
    
    def get_by_role(self, role):
        permissions = db.session.query(Permission).filter(Permission.role_reference == role).all()
        return [permission.to_dict() for permission in permissions]
    
    def get_by_reference(self, reference):
        permission = db.session.query(Permission).filter(Permission.reference == reference).first()
        return permission.to_dict() if permission else None
    
    def create(self, permission_data):
        permission = Permission(**permission_data.dict())
        db.session.add(permission)
        db.session.commit()
        db.session.refresh(permission)
        return permission.to_dict()
    
    def update(self, id: int, permission_data):
        permission = db.session.query(Permission).filter_by(id=id).first()
        if permission:
            for key, value in permission_data.items():
                setattr(permission, key, value) 
            db.session.commit()
            return permission.to_dict()
        return None
    
    def delete(self, id: int):
        permission = db.session.query(Permission).get(id)
        if permission:
            db.session.delete(permission)
            db.session.commit()
            return True
        return False
