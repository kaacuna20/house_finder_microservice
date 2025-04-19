from abc import ABC, abstractmethod

class IRoleService(ABC):
    @abstractmethod
    def GetAll(self):
        pass 

    @abstractmethod
    def GetById(self, id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, data, pk):
        pass

    @abstractmethod
    def delete(self, pk):
        pass