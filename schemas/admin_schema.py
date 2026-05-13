from pydantic import BaseModel
class ResponseAdmin(BaseModel):
    name_admin : str
    email : str
    user_name : str
    password : str
    is_write : bool
    changer_access : bool

class NewAdmin(BaseModel):
    name_admin : str
    email : str
    user_name : str
    password : str
    is_write : bool
    changer_access : bool

class UpdateAdmin(BaseModel):
    name_admin : str
    email : str
    user_name : str
    password : str
    is_write : bool
    changer_access : bool