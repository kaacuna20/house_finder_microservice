from abc import ABC, abstractmethod


class IMunicipalityService(ABC):
    
    @abstractmethod
    def getAll(self):
        pass
    
    @abstractmethod
    def getByCode(self, code: str):
        pass
    
    @abstractmethod
    def create(self, data):
        pass
    
    @abstractmethod
    def update(self, id: int, data):
        pass
    
    @abstractmethod
    def delete(self, id: int):
        pass