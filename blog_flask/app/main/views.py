#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template
from . import main
from .. import db
from ..model import Post, Comment
from flask_login import login_required, current_user
from app.auth.forms import CommentForm,PostForm

@main.route("/")
def home():
    return render_template('model_child.html', title=u"form")

@main.route('/service/')
def service():
    return 'service'

@main.route('/about/')
def about():
    return 'about'

@main.route('/product')
def product():
    return 'product'

@main.route('/post/<int:id>',methods=['Get','Post'])
def post(id):
    #Detail 详细页
    post = Post.query.get_or_404(id)
    #评论窗口
    form = CommentForm()
    #保存评论
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post)
        db.session.add(comment)
        db.session.commit()
    #评论列表
    return render_template('post/detail.html',
                           title=post.title,
                           form=form,
                           post=post)
@main.route('/edit')
@main.route('/edit/<int:id', methods=['GET','POST'])
@login_required
def edit(id = 0):
    form = PostForm

    if id == 0:
        post = Post(author=current_user)
    else:
        #修改
        post = Post.query.get_or_404(id)
    if form.validate_on_submit():
        post.body=form.body.data
        post.title = form.title.data

        db.session.add(post)
        db.session.commit()
    mode = u'添加'

    if id > 0:
        mode=u'编辑'
    return render_template('posts/edit.html',
                            title=u'编辑-%s' % post.title,
                            form=post,
                            post=post)

