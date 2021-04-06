from flask_login import UserMixin
from app import db,log_in
from datetime import datetime
class User(UserMixin,db.Model):
    __tablename__ = "Userinfo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('Upload',backref='author',lazy='dynamic')
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password




class Upload(UserMixin,db.Model):
    __tablename__ = "uploadata"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),nullable=False)
    about = db.Column(db.String(500),nullable=False)
    pic = db.Column(db.String(200),nullable=False)
    time = db.Column(db.DateTime,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey('Userinfo.id'))

@log_in.user_loader
def load_user(id):
    return User.query.get(int(id))