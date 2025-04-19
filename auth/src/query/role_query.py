from src.database.db_conection import db
from src.models.role_model import Role


class RoleQuery:
    
    def getAll(self):
        roles = db.session.query(Role).all()
        return [role.to_dict() for role in roles]
    
    def get_by_id(self, id: int):
        role = db.session.query(Role).get(id)
        return role.to_dict() if role else None
    
    def create(self, role_data):
        role = Role(**role_data.dict())
        db.session.add(role)
        db.session.commit()
        return role.to_dict()
    
    def update(self, id: int, role_data):
        role = db.session.query(Role).filter_by(id=id).first()
        for key, value in role_data.items():
            setattr(role, key, value)
        db.session.commit()
        return role.to_dict()
    
    def delete(self, id: int):
        role = db.session.query(Role).get(id)
        if role:
            db.session.delete(role)
            db.session.commit()
            return True
        return False
