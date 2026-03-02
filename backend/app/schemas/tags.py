from pydantic import BaseModel, Field, ConfigDict

class TagsBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Tags name")
    slug: str = Field(..., min_length=1, max_length=100, description="URL-friendly tags name")

class TagsCreate(TagsBase):
    pass

class TagsResponse(TagsBase):
    id: int = Field(..., description="Unique tags ID")

    model_config = ConfigDict(from_attributes=True)