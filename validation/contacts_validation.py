from pydantic import BaseModel, EmailStr, Field, ValidationError

from enum import Enum


class ContactCategory(str, Enum):
    FRIENDS = 'FRIENDS'
    FAMILY = 'FAMILY'
    WORKER = 'WORKER'



class ContactValidation(BaseModel):
    id: str = Field(min_length=36)
    name: str = Field(...)
    email: EmailStr = Field(..., max_length=100, min_length=10)
    phone: str = Field(...)
    address: str = Field(...)
    category: ContactCategory = Field(...)