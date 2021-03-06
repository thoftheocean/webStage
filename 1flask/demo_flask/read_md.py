#coding:utf-8
from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from livereload import Server
from markdown import markdown


app = Flask(__name__)

@app.route('/')
def first():
    return render_template('index1.html', title='hello', body1='##Header2')

@app.template_filter('md')
def markdown_to_html(txt):
    return markdown(txt)

def read_md(filename):
    with open(filename) as md_file:
        content = reduce(lambda x, y: x+y, md_file.read())
    return content.decode('utf-8')

@app.context_processor
def inject_methods():
    return dict(read_md=read_md)


if __name__=='__main__':
    # live_server=Server(app.wsgi_app)
    # live_server.watch('**/*.*')
    # live_server.serve(open_url=True)
    app.run(debug=True)

