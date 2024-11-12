from pydantic import BaseModel
from datetime import datetime

class CreateReaction(BaseModel):
    type: str
    user_id: int
    joke_id: int
    
    
class ReactionResponse(CreateReaction):
    id:int
    created_at:  datetime 
    
    #Config.from_attributes = True позволяет Pydantic работать с объектами SQLAlchemy.
    class Config:
        from_attributes = True