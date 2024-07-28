from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Union
from typing_extensions import Annotated
from uuid import UUID
from enum import Enum


class UserType(str, Enum):
    admin = 'admin'
    user = 'user'


class SignUpSchema(BaseModel):
    username: str
    password: str
    email: EmailStr
    company: str
    contact_number: str
    company_logo_url: str
    company_slogan: str
    user_type:  Annotated[Union[UserType, None],
                          Field(alias='user_type')] = None

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    username: str
    password: str
