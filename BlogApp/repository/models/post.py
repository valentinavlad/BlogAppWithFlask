from datetime import datetime
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Date, ForeignKey
from setup.db_connect import Base

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=False, nullable=False)
    owner = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    contents = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.utcnow)
    modified_at = Column(Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Post(title='{}', owner='{}', created_at={})>"\
                .format(self.title, self.owner, self.created_at)
