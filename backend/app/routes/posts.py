from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.posts_service import PostsService
from ..schemas.posts import PostsResponse, PostsListResponse

router = APIRouter(
    prefix="/api/posts",
    tags=['posts']
)

@router.get("", response_model=PostsListResponse, status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    service = PostsService(db)
    return service.get_all_posts()

@router.get("/{posts_id}", response_model=PostsResponse, status_code=status.HTTP_200_OK)
def get_posts_id(posts_id: int, db: Session = Depends(get_db)):
    service = PostsService(db)
    return service.get_posts_by_id(posts_id)

@router.get("/tags/{tags_id}", response_model=PostsListResponse, status_code=status.HTTP_200_OK)
def get_posts_by_tags(tags_id: int, db: Session = Depends(get_db)):
    service = PostsService(db)
    return service.get_posts_by_tags(tags_id)