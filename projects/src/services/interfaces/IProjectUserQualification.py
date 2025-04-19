from abc import ABC, abstractmethod


class IProjectUserQualification(ABC):
    
    @abstractmethod
    def get_qualifications_by_user(self, user: str) -> list:
        """Get the qualification of a user by their email."""
        pass

    @abstractmethod
    def get_qualifications_by_project(self, project_slug: str) -> list:
        """Get the qualifications of a project by its slug."""
        pass

    @abstractmethod
    def create(self, data) -> dict:
        """Create a new project user qualification."""
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        """Delete a project user qualification by ID."""
        pass