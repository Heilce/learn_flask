# -*- coding:utf-8 -*-
# author: xip tim:2018/3/30

from user_Form import MyForm, Register
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import make_response
from flask import redirect
from flask import abort
from model import app, db, User
from flask import flash


@app.route('/', methods=['get', 'post'])
def login(name=None):
    print("******")
    form1 = MyForm()
    form2 = Register()
    if form1.validate_on_submit():
        name = form1.name.data
        password = form1.password.data
        user = User.query.filter_by(name=form1.name.data).first()
        if user is None:
            flash("该用户名不存在，请重新输入")
        else:
            if password == user.password:
                return render_template('index.html')
            else:
                flash("密码不正确请重新输入密码")
        # 对于登录的逻辑判断，我们现在处理的是注册的情况
    if form2.validate_on_submit():
        name = form2.name.data
        password = form2.password1.data
        user = User(name=name, password=password)
        db.session.add(user)
        db.session.commit()
    return render_template('login.html', form1=form1, form2=form2)


if __name__ == '__main__':
    # 删除表
    app.debug = True
    app.run()
