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