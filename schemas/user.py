from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    
    
class UserResponse(UserCreate):
    id: int
    created_at: datetime    
    
    #Config.from_attributes = True позволяет Pydantic работать с объектами SQLAlchemy.
    class Config:
        from_attributes = True