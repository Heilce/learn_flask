# -*- coding:utf-8 -*-
# author: xip tim:2018/4/2

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField,SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('用户名：', validators=[DataRequired()])
    password = PasswordField('密&nbsp;&nbsp;&nbsp;码:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Register(FlaskForm):
    name = StringField('用户名：', validators=[DataRequired()])
    password1 = PasswordField('密码：', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField()
