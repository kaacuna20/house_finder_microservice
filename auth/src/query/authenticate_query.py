from src.database.db_conection import db
from src.models.user_model import User


class AuthenticateQuery:
    def get_user_by_email(self, email: str) -> User:
        """Retrieve a user by their email."""
        user = db.session.query(User).filter_by(email=email).first()
        return user

    def get_user_by_id(self, user_id: int) -> User:
        """Retrieve a user by their ID."""
        user = db.session.query(User).filter_by(id=user_id).first()
        return user