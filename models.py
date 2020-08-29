from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True, unique=True)
    text = Column(String)
    link = Column(String, unique=True)


class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True, unique=True)
    text = Column(String)
    link = Column(String, unique=True)
    post = Column(Integer, ForeignKey('posts.post_id'))
