#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, flash

def init_views(app):
    @app.route("/")
    def home():
        return render_template('model_child.html', title=u"form")

    @app.route('/service/')
    def service():
        return 'service'

    @app.route('/about/')
    def about():
        return 'about'

    @app.route('/product')
    def product():
        return 'product'


    @app.route('/login/', methods=['GET','POST'])
    def login():
        from .forms import LoginForm
        form = LoginForm()
        flash(u'登录成功')
        return render_template('loginform.html', title='登录', form=form)

