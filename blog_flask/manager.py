from flask.ext.script import Manager
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand,upgrade

app = create_app()

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


#新增加一个检测文件的指令  #运行 python demo.py dev
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)

@manager.command
def test():
    pass

@manager.command
def deploy():
    from app.model import Role
    upgrade()
    Role.seed()


if __name__ == "__main__":

    #普通模式
    # app.run()

    #设调试模式

    app.run(debug=True)


    #实时监控模式 运行 python demo.py runserver
    # manager.run()