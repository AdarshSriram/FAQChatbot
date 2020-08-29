from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///corpus.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True, unique=True)
    text = Column(String)
    link = Column(String, unique=True)
    lemmatized_text = Column(String)


class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True, unique=True)
    text = Column(String)
    link = Column(String, unique=True)
    post = Column(Integer, ForeignKey('posts.post_id'))
