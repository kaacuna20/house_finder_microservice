from src.database.db_conection import db
from src.models.municipality_model import Municipality


class MunicipalityQuery:
    
    def getAll(self):
        municipalities = db.session.query(Municipality).all()
        return [m.to_dict() for m in municipalities]
    
    def get_by_code(self, code: str):
        municipality = db.session.query(Municipality).filter(Municipality.divipola_code == code).first()
        if municipality:
            return municipality.to_dict()
        return None
    
    def create(self, data):
        municipality = Municipality(**data.dict())
        municipality.save()
        return municipality.to_dict()
    
    def update(self, id: int, data):
        municipality = db.session.query(Municipality).filter(Municipality.id == id).first()
        for key, value in data.dict(exclude_unset=True).items():
            setattr(municipality, key, value)
        db.session.commit()
        db.session.refresh(municipality)
        return municipality.to_dict()
    
    def delete(self, id: int):
        municipality = db.session.query(Municipality).filter(Municipality.id == id).first()
        if municipality:
            db.session.delete(municipality)
            db.session.commit()
            return True
        return False
    