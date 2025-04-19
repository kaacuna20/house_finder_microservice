from src.models.user_model import User
from src.database.db_conection import db


class UserQuery:
    
    def get_all(self):
        users = db.session.query(User).all()
        return [user.to_dict() for user in users]


    def get_by_id(self, id: int):
        user = db.session.query(User).get(id)
        return user.to_dict()

        
    def create(self, user_data):
        user = User(**user_data.dict())
        user.save()
        return user.to_dict()

        
    def update(self, id: int, user_data):
        user = db.session.query(User).filter_by(id=id).first()
        for key, value in user_data.items():
            setattr(user, key, value) 
        db.session.commit()
        return user.to_dict()

    def delete(self, id: int):
        user = db.session.query(User).get(id)
        db.session.delete(user)
        db.session.commit()
        return True
