from pydantic import BaseModel
from datetime import datetime



class JokeCreate(BaseModel):
    content: str
    user_id: int
    category_id: int
    
    
class JokeResponse(JokeCreate):
    id: int
    created_at: datetime  
    
    #Config.from_attributes = True позволяет Pydantic работать с объектами SQLAlchemy.
    class Config:
        from_attributes = True