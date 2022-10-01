#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
#Python
from typing import Optional

class ContactSchema(BaseModel):
    id: Optional[str] 
    name: str 
    email: EmailStr 
    comment: str 