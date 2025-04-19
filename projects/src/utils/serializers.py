from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Optional, List


class CreateProject(BaseModel):
    name: str = Field(..., description="Project name", max_length=255)
    logo: Optional[HttpUrl] = Field(None, description="Logo URL", max_length=500)
    description: Optional[str] = Field(None, description="Project description")
    location: str = Field(None, description="Location", max_length=255)
    municipality_divipola: str = Field(None, description="Municipality divipola code", max_length=100)
    company_nit: str = Field(None, description="Company NIT", max_length=100)
    address: Optional[str] = Field(None, description="Address", max_length=255)
    contact: Optional[str] = Field(None, description="Contact information", max_length=255)
    area: float = Field(None, description="Area in square meters", ge=0)
    price: int = Field(None, description="Price", ge=0)
    type: Optional[str] = Field(None, description="Type of project", max_length=100)
    img_url: Optional[HttpUrl] = Field(None, description="Image URL", max_length=500)
    url_website: HttpUrl = Field(None, description="Website URL", max_length=255)
    latitude: float = Field(None, description="Latitude")
    longitude: float = Field(None, description="Longitude")

    model_config = {
        "from_attributes": True
    }
    

class CreateMunicipality(BaseModel):
    name: str = Field(..., description="Municipality name", max_length=255)
    divipola_code: str = Field(..., description="Municipality divipola code", max_length=100)

    model_config = {
        "from_attributes": True
    }
    
    
class CreateCompany(BaseModel):
    name: str = Field(..., description="Company name", max_length=255)
    nit: str = Field(..., description="Company NIT", max_length=100)
    address: Optional[str] = Field(None, description="Address", max_length=255)
    contact: Optional[str] = Field(None, description="Contact information", max_length=255)

    model_config = {
        "from_attributes": True
    }
    

class CreateProjectUserQualification(BaseModel):
    user_ref: EmailStr = Field(description="User email", max_length=255)
    project_ref: str = Field(..., description="Project slug", max_length=255)
    qualification: float = Field(..., description="Qualification rating", ge=0, le=5)

    model_config = {
        "from_attributes": True
    }