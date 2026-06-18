from pydantic import BaseModel, Field, ConfigDict, AliasChoices
from pydantic.alias_generators import to_camel
from typing import Optional


class BaseAdminModel(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        validate_default=True,
        validate_by_alias=True,
        alias_generator=to_camel,
        populate_by_name=True,
        extra="forbid",
    )


class ResponseAdmin(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )
    name_admin: str
    email: str
    user_name: str
    is_write: bool
    changer_access: bool
    id: int


class NewAdmin(BaseAdminModel):
    name_admin: str = Field(
        "ali",
        min_length=2,
        validation_alias=AliasChoices("nameAdmin", "Nameadmin", "NameAdmin"),
        serialization_alias="nameAdmin"
    )

    email: str = "ali124@gmail.com"
    user_name: str = Field("MrALI", min_length=3)
    password: str = Field(min_length=8)
    is_write: bool = False
    changer_access: bool = False


class UpdateAdmin(BaseAdminModel):

    name_admin: Optional[str] = Field(None, min_length=2)
    email: Optional[str] = None
    user_name: Optional[str] = Field(None, min_length=3)
    password: Optional[str] = Field(None, min_length=8)
    is_write: Optional[bool] = None
    changer_access: Optional[bool] = None
