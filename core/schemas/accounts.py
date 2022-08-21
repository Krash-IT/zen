import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, EmailStr, HttpUrl


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class RegisterUserSchema(BaseModel):
    email: EmailStr
    password: str


class UserDetailSchema(BaseModel):
    id: int
    email: EmailStr
    first_name: str = None
    last_name: str = None