from abc import ABC, abstractmethod


class IProjectService(ABC):
    
    def getAll(self) -> list:
        """
        Get all projects.
        """
        pass
    
    def getBySlug(self, slug: str) -> dict:
        """
        Get project by slug.
        """
        pass
    
    def create(self, data: dict) -> dict:
        """
        Create a new project.
        """
        pass
    
    def update(self, id: int, data: dict) -> dict:
        """
        Update an existing project.
        """
        pass
    
    def delete(self, id: int) -> dict:
        """
        Delete a project.
        """
        pass