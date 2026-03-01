from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
import re

class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)

    posts = relationship("Posts", back_populates="tags")

    def __repr__(self):
        return f"<Tags(id={self.id}, name='{self.name}')>"