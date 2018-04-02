# -*- coding:utf-8 -*-
# author: xip tim:2018/4/2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
# 设置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/flask_demo'
app.secret_key = 'flask is hard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    name = db.Column(db.String(16), primary_key=True)
    password = db.Column(db.String(16))
