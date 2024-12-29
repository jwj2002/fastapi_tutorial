from typing_extensions import Self
from typing import Optional, Any
from pydantic import BaseModel, model_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None
    
    @model_validator(mode='before')
    @classmethod
    def generate_slug(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data['slug'] = data['title'].replace(" ", "-").lower()
        return data
    
class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    create_at: datetime
    
    class Config():
        
        orm_mode = True
    