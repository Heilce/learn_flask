# -*- coding:utf-8 -*-
# author: xip tim:2018/4/2
from exts import db


class User(db.Model):
    __tablename__ = 'User'
    name = db.Column(db.String(16), primary_key=True)
    password = db.Column(db.String(16))
