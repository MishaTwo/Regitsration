from sqlalchemy import Column, Integer, String, Enum, Time, DateTime
from .base import BASE
from datetime import datetime
import enum


class Post(BASE):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now())
    title = Column(String(100), nullable=False)
    content = Column(String(100), nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content