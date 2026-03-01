from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.tags import Tags
from ..schemas.tags import TagsCreate

class TagsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Tags]:
        return self.db.query(Tags).all()
    
    def get_by_id(self, tags_id: int) -> Optional[Tags]:
        return self.db.query(Tags).filter(Tags.id  == tags_id).first()
    
    def get_by_slug(self, slug: str) -> Optional[Tags]:
        return self.db.query(Tags).filter(Tags.slug == slug).first()
    
    def create(self, tags_data: TagsCreate) -> Tags:
        db_tags = Tags(**tags_data.model_dump())
        self.db.add(db_tags)
        self.db.commit()
        self.db.refresh(db_tags)
        return db_tags