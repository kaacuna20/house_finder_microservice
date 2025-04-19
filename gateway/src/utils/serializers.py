from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any 


class CreateLog(BaseModel):
    name: str = Field(..., description="The name of the log entry")
    service: str = Field(..., description="The name of the service")
    causer: str = Field(..., description="The name of the causer")
    action: str = Field(..., description="The action performed")
    data: Optional[Dict[str, Any]] = Field(None, description="Additional data related to the log entry")
    
    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.dict().items() if v is not None}
    
    
class GetItemLog(BaseModel):
    name: Optional[str] = Field(None, description="The name of the log entry")
    service: Optional[str] = Field(None, description="The name of the service")
    causer: Optional[str] = Field(None, description="The name of the causer")
    action: Optional[str] = Field(None, description="The action performed")
    data: Optional[Dict[str, Any]] = Field(None, description="Additional data related to the log entry")
    
    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.dict().items() if v is not None}
    

class CreateRoute(BaseModel):
    module: Optional[str] = Field(None, description="The module of the service")
    service: Optional[str] = Field(None, description="The name of the service")
    method: Optional[str] = Field(None, description="The HTTP method used")
    path: Optional[str] = Field(None, description="The path of the request")
    action: Optional[str] = Field(None, description="The action performed")
    is_authenticated: Optional[bool] = Field(None, description="Whether authentication is required")
    
    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.dict().items() if v is not None}

  
class GetItemRoute(BaseModel):
    id: Optional[str] = Field(None, description="The ID of the route")  
    module: Optional[str] = Field(None, description="The ID of the service")
    service: Optional[str] = Field(None, description="The name of the service")
    method: Optional[str] = Field(None, description="The HTTP method used")
    path: Optional[str] = Field(None, description="The path of the request")
    action: Optional[str] = Field(None, description="The action performed")
    is_authenticated: Optional[bool] = Field(None, description="Whether authentication is required")
    
    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.dict().items() if v is not None}