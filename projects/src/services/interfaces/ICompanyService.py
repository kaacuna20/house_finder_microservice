from abc import ABC, abstractmethod


class ICompanyService(ABC):
    
    
    def getAll(self):
        """
        Get all companies
        """
        pass
    
    def getByNit(self, nit):
        """
        Get company by nit
        """
        pass
    
    def create(self, data):
        """
        Create company
        """
        pass
    
    def update(self, id, data):
        """
        Update company
        """
        pass
    
    def delete(self, id):
        """
        Delete company
        """
        pass
    
    