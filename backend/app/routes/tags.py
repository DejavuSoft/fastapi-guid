from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.tags_service import TagsService
from ..schemas.tags import TagsResponse

router = APIRouter(
    prefix="/api/tags",
    tags=['tags']
)

@router.get("", response_model=List[TagsResponse], status_code=status.HTTP_200_OK)
def get_tags(db: Session = Depends(get_db)):
    service = TagsService(db)
    return service.get_all_tags()

@router.get("/{tags_id}", response_model=TagsResponse, status_code=status.HTTP_200_OK)
def get_tags_id(tags_id: int, db: Session = Depends(get_db)):
    service = TagsService(db)
    return service.get_tags_by_id(tags_id)
