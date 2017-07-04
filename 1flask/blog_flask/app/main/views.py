#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for,current_app,abort
from . import main
from .. import db
from ..model import Post, Comment
from flask_login import login_required, current_user
from app.auth.forms import CommentForm, PostForm
from flask_babel import gettext as _

@main.route("/")
def home():

    page_home = request.args.get('page', 1, type=int)
    query = Post.query.order_by(Post.created.desc())
    pagination = query.paginate(page_home, per_page=20, error_out=False)
    posts = pagination.items
    return render_template('index2.html',
                           title=u"欢迎来到H的博客",
                           post=posts,
                           pagination=pagination)

@main.route('/service/')
def service():
    return 'service'

@main.route('/about/')
def about():
    return 'about'

@main.route('/product')
def product():
    return 'product'

@main.route('/post/<int:id>', methods=['Get', 'Post'])
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
    return render_template('posts/detail.html',
                            title=post.title,
                            form=form,
                            post=post)

@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
def edit(id=0):
    form = PostForm()

    # if id == 0:
    #     post = Post(author=current_user)
    #
    # else:
    #     post = Post.query.get_or_404(id)


    # if id == 0:
    #     post = Post(author='thoftheocean')
    #
    # else:
    #     post = Post.query.get_or_404(id)
    post = Post()

    if form.validate_on_submit():
        post.body = form.body.data
        post.title = form.title.data

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('.post', id=post.id))

    form.title.data = post.title
    form.body.data = post.body

    title = _(u'添加新文章')
    if id > 0:
        title = _(u'编辑 - %(title)', title=post.title)

    return render_template('posts/edit.html',
                           title=title,
                           form=form,
                           post=post)


# @main.route('/shoutdown')
# def shutdown():
#     if not current_app.testing:
#         abort(404)
#
#     shoutdown = request.environ.get('werkzeug.server.shutdown')
#     if not shoutdown:
#         abort(500)
#
#     shoutdown()
#     return u'正在关闭服务端进程...'
