from datetime import datetime
from models.db import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(255))
    temperature = db.Column(db.Integer)
    summary = db.Column(db.String(80))
    icon_source = db.Column(db.String(80))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.now())

    def __init__(self, name, location, content, temperature, summary, icon_source):
        self.name = name
        self.location = location
        self.content = content
        self.temperature = temperature
        self.summary = summary
        self.icon_source = icon_source

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "content": self.content,
            "temperature": self.temperature,
            "summary": self.summary,
            "icon_source": self.icon_source,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Post.query.all()

    @classmethod
    def find_by_id(cls, post_id):
        return Post.query.filter_by(id=post_id).first()
