from pydantic import BaseModel, Field

class TagsBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Tags name")
    slug: str = Field(..., min_length=5, max_length=100, description="URL-friendly tags name")

class TagsCreate(TagsBase):
    pass

class TagsResponse(TagsBase):
    id: int = Field(..., description="Unique tags ID")

    class Config:
        form_attributes = True