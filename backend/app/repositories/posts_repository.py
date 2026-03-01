from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from ..models.posts import Posts
from ..schemas.posts import PostsCreate

class TagsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Posts]:
        return self.db.query(Posts).options(joinedload(Posts.tags)).all()
    
    def get_by_id(self, posts_id: int) -> Optional[Posts]:
        return self.db.query(Posts).options(joinedload(Posts.tags)).filter(Posts.id  == posts_id).first()
    
    def get_by_tags(self, tags_id: str) -> Optional[Posts]:
        return self.db.query(Posts).options(joinedload(Posts.tags)).filter(Posts.tags_id == tags_id).first()
    
    def create(self, posts_data: PostsCreate) -> Posts:
        db_posts = Posts(**posts_data.model_dump())
        self.db.add(db_posts)
        self.db.commit()
        self.db.refresh(db_posts)
        return db_posts
    
    def get_multiple_by_ids(self, posts_ids: List[int]) -> List[Posts]:
        return (
            self.db.query(Posts).options(joinedload(Posts.tags)).filter(Posts.id.in_(posts_ids)).all()
        )