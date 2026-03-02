from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing  import Optional
from .tags import TagsResponse

class PostsBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description="Posts name")
    description: Optional[str] = Field(None, min_length=5, max_length=200, description="Description posts")
    content: Optional[str] = Field(None, min_length=200, max_length=3000, description="Content posts")
    tags_id: int = Field(..., description="Tags ID")
    image_url: Optional[str] = Field(None, description="Posts image URL")

class PostsCreate(PostsBase):
    pass

class PostsResponse(BaseModel):
    id: int = Field(..., description="Unique posts ID")
    name: str
    description: Optional[str]
    content: Optional[str]
    tags_id: int
    image_url: Optional[str]
    create_at: datetime
    tags: TagsResponse = Field(..., description="Posts tags")

    model_config = ConfigDict(from_attributes=True)

class PostsListResponse(BaseModel):
    posts: list[PostsResponse]
    total: int = Field(..., description="Total number of totals posts")