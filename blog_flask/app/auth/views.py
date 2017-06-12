#coding=utf-8
from flask import render_template, request, flash, redirect, url_for
from . import auth
from .forms import LoginForm, RegistrationForm
from ..model import User
from .. import db
from flask_login import login_user, logout_user, current_user



@auth.route('/login/', methods=['GET', 'POST'])
def login():
    from .forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name = form.username.data).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('main.home'))

    return render_template('loginform.html', title='登录', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register/', methods=['GET','POSt'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.submit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', title=u'注册', form=form)