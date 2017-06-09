#coding:utf-8
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_nav import *
from flask_nav.elements import *
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)

#模板
Bootstrap(app)

#导航栏
nav = Nav(app)
nav.register_element('top', Navbar(
                                 View(u'主页', 'home'),
                                 View(u'关于', 'about'),
                                 View(u'服务', 'service'),
                                 View(u'产品', 'product'),
                                  ))
nav.init_app(app)


@app.route("/")
def home():
    return render_template('model_child.html', title=u"模板")

@app.route('/service/')
def service():
    return 'service'

@app.route('/about/')
def about():
    return 'about'

@app.route('/product')
def product():
    return 'product'

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