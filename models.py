import re
from datetime import datetime

from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
)
from sqlalchemy.orm import backref, relationship

from app import db


def slugify(s):
    pattern = r"[^\w+]"
    return re.sub(pattern, "-", s)


post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship(
        "Tag", secondary=post_tags, backref=db.backref("posts", lazy="dynamic")
    )

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self) -> str:
        return "{}-{}".format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return "{}".format(self.name)


class Lessons(db.Model):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_lessons = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "{} - {}".format(self.name, self.date_lessons)


user_lessons_m2m = db.Table(
    "user_lessons",
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("lessons_id", db.ForeignKey("lessons.id"), primary_key=True),
)


##### Flask-sec #####


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    permissions = Column(UnicodeText)


class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    first_name = Column(String(100))
    pic_url = Column(String(100), nullable=True)
    last_name = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())

    fs_uniquifier = Column(String(255), unique=True, nullable=False)
    confirmed_at = Column(DateTime())
    roles = relationship(
        "Role", secondary="roles_users", backref=backref("users", lazy="dynamic")
    )
    lessons = db.relationship(
        "Lessons",
        secondary=user_lessons_m2m,
        backref=db.backref("users", lazy="dynamic"),
    )
