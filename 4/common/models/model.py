# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()
from application import db



class News(db.Model):
    __tablename__ = 'news'

    title = db.Column(db.String(45, 'utf8mb4_0900_ai_ci'), primary_key=True, nullable=False)
    url = db.Column(db.String(100), primary_key=True, nullable=False)



class News2(db.Model):
    __tablename__ = 'news2'

    title = db.Column(db.String(200, 'utf8mb4_0900_ai_ci'))
    url = db.Column(db.String(200), primary_key=True)
    department = db.Column(db.String(45, 'utf8mb4_0900_ai_ci'))
    publishdate = db.Column(db.String(45))
    count = db.Column(db.String(45))
    content = db.Column(db.String(9000, 'utf8mb4_0900_ai_ci'))
    piclinks = db.Column(db.String(9000))
