from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique = True,index = True)
    username= db.Column(db.String(150),index = True)
    password =  db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone =True),default = func.now())
    posts = db.relationship('Post',backref = 'user',passive_deletes = True)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key = True)
    text = db.Column(db.String,nullable = False)
    date_created = db.Column(db.DateTime(timezone =True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('user.id',ondelete = 'CASCADE'),nullable = False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    text = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime(timezone =True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('user.id',ondelete = 'CASCADE'),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id',ondelete = 'CASCADE'),nullable = False)



