"""User-related Pydantic schemas."""

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    """Base user schema with shared fields."""

    username: str
    email: EmailStr
    name: str
    age: int | None = None
    address: str | None = None
    phone_no: str | None = None


class UserCreate(UserBase):
    """Schema for user registration."""

    password: str


class UserResponse(UserBase):
    """Schema for user responses."""

    model_config = ConfigDict(from_attributes=True)

    id: int


class UserLogin(BaseModel):
    """Schema for user login."""

    username: str
    password: str


class Token(BaseModel):
    """Schema for authentication token response."""

    access_token: str
    token_type: str = "bearer"
