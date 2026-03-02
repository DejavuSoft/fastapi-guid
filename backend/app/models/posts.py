from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    autor = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    tags_id = Column(Integer, ForeignKey("tags.id"), nullable=False)
    description = Column(Text)
    content = Column(Text)
    image_url = Column(String, index=True)
    create_at = Column(DateTime, default=datetime.utcnow)

    tags = relationship("Tags", back_populates="posts")

    def __repr__(self):
        return f"<Posts(id={self.id}, name='{self.name}', description='{self.description}')>"