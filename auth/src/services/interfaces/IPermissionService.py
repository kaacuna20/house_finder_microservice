from abc import ABC, abstractmethod


class IPermisionService(ABC):

    @abstractmethod
    def get_permissions_by_role(self, role):
        """
        Get permissions for a given role reference.
        :param role_refernece: The REFERENCE of the role to get permissions for.
        :return: A list of permissions for the role.
        """
        pass
    
    @abstractmethod
    def get_permissions_by_reference(self, reference):
        """
        Get permissions by their reference.
        :param reference: The reference of the permission to retrieve.
        :return: The permission object if found, None otherwise.
        """
        pass
    
    # @abstractmethod
    # def check_permission_by_role(self, role_reference, permission):
    #     """
    #     Check if a role has a specific permission.
    #     :param role_id: The ID of the role to check permissions for.
    #     :param permission: The permission to check for.
    #     :return: True if the role has the permission, False otherwise.
    #     """
    #     pass
    
    @abstractmethod
    def create(self, data):
        """
        Create a new permission.
        :param permission_data: A dictionary containing the permission data.
        :return: The created permission object.
        """
        pass
    
    @abstractmethod
    def update(self, data, pk):
        """
        Update an existing permission.
        :param permission_id: The ID of the permission to update.
        :param permission_data: A dictionary containing the updated permission data.
        :return: The updated permission object.
        """
        pass
    
    @abstractmethod
    def delete(self, pk):
        """
        Delete a permission by its ID.
        :param permission_id: The ID of the permission to delete.
        :return: True if the permission was deleted, False otherwise.
        """
        pass




