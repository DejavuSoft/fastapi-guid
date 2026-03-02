from sqlalchemy.orm import Session
from typing import List
from ..repositories.posts_repository import PostsRepository
from ..repositories.tags_repository import TagsRepository
from ..schemas.posts import PostsResponse, PostsListResponse, PostsCreate
from fastapi import HTTPException, status

class PostsService:
    def __init__(self, db: Session):
        self.posts_repository = PostsRepository(db)
        self.tags_repository = TagsRepository(db)

    def get_all_posts(self) -> PostsListResponse:
        posts = self.posts_repository.get_all()
        posts_response = [PostsResponse.model_validate(pos) for pos in posts]
        return PostsListResponse(posts=posts_response, total=len(posts_response))
    
    def get_posts_by_id(self, posts_id: int) -> PostsResponse:
        posts = self.posts_repository.get_by_id(posts_id)
        if not posts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Posts with id {posts_id} not found"
            )
        return PostsResponse.model_validate(posts)
    
    def get_posts_by_tags(self, tags_id: int) -> PostsListResponse:
        tags = self.tags_repository.get_by_id(tags_id)
        if not tags:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Tags with id {tags_id} does not exist"
            )
        
        posts = self.posts_repository.get_by_tags(tags_id)
        posts_response = [PostsResponse.model_validate(pos) for pos in posts]
        return PostsListResponse(posts=posts_response, total=len(posts_response))
    
    def create_tags(self, posts_data: PostsCreate) -> PostsResponse:
        posts = self.posts_repository.create(posts_data)
        return PostsResponse.model_validate(posts)