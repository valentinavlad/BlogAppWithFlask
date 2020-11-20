from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Date
from sqlalchemy.orm import relationship
from setup.db_connect import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.utcnow)
    modified_at = Column(Date, nullable=False, default=datetime.utcnow)

    posts = relationship('Post', backref='users', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return '<User %r>' % self.name
