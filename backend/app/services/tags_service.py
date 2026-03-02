from sqlalchemy.orm import Session
from typing import List
from ..repositories.tags_repository import TagsRepository
from ..schemas.tags import TagsResponse, TagsCreate
from fastapi import HTTPException, status

class TagsService:
    def __init__(self, db: Session):
        self.repository = TagsRepository(db)

    def get_all_tags(self) -> List[TagsResponse]:
        tags = self.repository.get_all()
        return [TagsResponse.model_validate(tag) for tag in tags]
    
    def get_tags_by_id(self, tags_id: int) -> TagsResponse:
        tags = self.repository.get_by_id(tags_id)
        if not tags:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tags with id {tags_id} not found")
        return TagsResponse.model_validate(tags)
    
    def create_tags(self, tags_data: TagsCreate) -> TagsResponse:
        tags = self.repository.create(tags_data)
        return TagsResponse.model_validate(tags)