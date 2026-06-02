from pydantic import BaseModel
from typing import Optional


class ResponseAdmin(BaseModel):
    name_admin: str
    email: str
    user_name: str
    password: str
    is_write: bool
    changer_access: bool


class NewAdmin(BaseModel):
    name_admin: str = "ali"
    email: str = "ali124@gmail.com"
    user_name: str = "MrALI"
    password: int | str
    is_write: bool = False
    changer_access: bool = False


class UpdateAdmin(BaseModel):
    name_admin: Optional[str] = None
    email: Optional[str] = None
    user_name: Optional[str] = None
    password: Optional[str] = None
    is_write: Optional[bool] = None
    changer_access: Optional[bool] = None
