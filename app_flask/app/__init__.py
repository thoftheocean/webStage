#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask

from flask_bootstrap import Bootstrap
from flask_nav import *
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy

from .view import init_views

#获取当前文件的决定路径
from os import path
basedir = path.abspath(path.dirname(__file__))

#模板
bootstrap = Bootstrap()
#数据库
db = SQLAlchemy()
#导航栏
nav = Nav()




def create_app():
    app = Flask(__name__)
    # # 读取外部的配置文件
    app.config.from_pyfile('config')
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    nav.register_element('top', Navbar(
        View(u'主页', 'home'),
        View(u'关于', 'about'),
        View(u'服务', 'service'),
        View(u'产品', 'product'),
    ))
    db.init_app(app)
    bootstrap.init_app(app)
    nav.init_app(app)
    init_views(app)
    return app


