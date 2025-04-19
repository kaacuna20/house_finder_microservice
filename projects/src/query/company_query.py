from src.models.company_model import Company
from src.database.db_conection import db


class CompanyQuery:
    
    def getAll(self):
        companies = db.session.query(Company).all()
        return [company.to_dict() for company in companies]
    
    def get_by_nit(self, nit: str):
        company = db.session.query(Company).filter(Company.nit == nit).first()
        if company:
            return company.to_dict()
        return None
    
    def create(self, data):
        company = Company(**data.dict())
        company.save()
        return company.to_dict()
    
    def update(self, id: int, data):
        company = db.session.query(Company).filter(Company.id == id).first()
        for key, value in data.dict(exclude_unset=True).items():
            setattr(company, key, value)
        db.session.commit()
        db.session.refresh(company)
        return company.to_dict()
    
    def delete(self, id: int):
        company = db.session.query(Company).filter(Company.id == id).first()
        if company:
            db.session.delete(company)
            db.session.commit()
            return True
        return False
    