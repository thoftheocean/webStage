#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename
from flask_script import Manager
from os import path


app = Flask(__name__)
manager = Manager(app)

@app.route("/")
#cookies 设置

def hello():
    # abort(400) #直接返回400
    responses = make_response(render_template('model_child.html',title="何喜  hao"))
    responses.set_cookie('username', '')
    return responses
#出现404错误，响应到指定的404页面
@app.errorhandler(404)
def page_not_find(error):
    return render_template('404.html'), 404


@app.route('/service')
def service():
    return 'service'

@app.route('/about')
def about():
    return 'about'



#定义动态的路由
#默认的转换器int float path
@app.route('/user1/<int:username>')
def user1(username):
    return 'user %s' % username

#重构一个正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
app.url_map.converters['regex'] = RegexConverter

@app.route('/user2/<regex("[a-z]{3}"):user_id>')
def user2(user_id):
    return 'user %s' % user_id


#两个地址都能访问到project页面
@app.route('/projects/')
@app.route('/project/')
def projects():
    return 'the project page'



@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


    return render_template('login.html', method=request.method)


#将文件信息传入到服务端
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        f.save(path.join(basepath, 'static\\uploads', secure_filename(f.filename)))
        return redirect(url_for('upload'))
    return render_template('upload.html')



# #自定义过滤器
# @app.template_filter('md')
# def markdown_to_html(txt):
#     from markdown import  markdown
#     return markdown(txt)
#
#

#



#指明输入参数的类型
# @app.route('/user/<int:user_id>')  #转换器：int float path
# def user(user_id):
#     return 'user %s' % user_id


#
#





    # if request.method == 'POST':
    #     f = request.files['file']
    #     basepath = path.abspath(path.dirname(__file__))
    #     f.save(path.join(basepath, 'static\uploads', secure_filename(f.filename)))
    #     return redirect(url_for('upload'))
    # return render_template('upload.html')




#新增加一个检测文件的指令  #运行 python demo.py dev
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

if __name__ == "__main__":

    #普通模式
    # app.run()

    #设调试模式
    app.run(debug=True)

    #实时监控模式 运行 python demo.py runserver
    # manager.run()