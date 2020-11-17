from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.utcnow)
    modified_at = Column(Date, nullable=False, default=datetime.utcnow)

    posts = relationship('Post', backref='users', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name
