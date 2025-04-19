from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List


class CreateUser(BaseModel):
    email: EmailStr
    password: str
    is_active: bool = Field(default=True, description="User's active status")
    is_super_user: bool = Field(default=False, description="User's superuser status")
    role_reference: str = Field(..., description="Role reference for the user")

    model_config = {
        "from_attributes": True
    }
    
class UpdateUser(BaseModel):
    email: Optional[EmailStr] = Field(None, description="User's email")
    is_active: Optional[bool] = Field(None, description="User's active status")
    role_reference: Optional[str] = Field(None, description="Role reference for the user")
    
    model_config = {
        "from_attributes": True
    }
    
    
class AuthUser(BaseModel):
    email: EmailStr
    password: str
    
    model_config = {
        "from_attributes": True
    } 
        
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class CreateRole(BaseModel):
    reference: str = Field(..., description="Role reference")
    name: str = Field(..., description="Role name", max_length=255)
    is_active: bool = Field(default=True, description="Role's active status")
    description: str = Field(..., description="Role description")
    
    model_config = {
        "from_attributes": True
    }
        

class CreatePermision(BaseModel):
    reference: str = Field(..., description="Permission reference")
    name: str = Field(..., description="Permission name", max_length=255)
    is_active: bool = Field(default=True, description="Permission's active status")
    service: str = Field(..., description="Service name")
    module: str = Field(..., description="Module name")
    actions: List[str] = Field(..., description="List of actions")
    role_reference: str = Field(..., description="Role reference for the permission")   
    
    model_config = {
        "from_attributes": True
    }
        
        
class UserRolePermissions(BaseModel):
    id: int
    email: EmailStr
    role: List[CreateRole] = []  # List of roles associated with the user
    is_active: bool
    is_super_user: bool
    permissions: List[CreatePermision] = []  # List of permissions associated with the user
    
    model_config = {
        "from_attributes": True
    }
        
