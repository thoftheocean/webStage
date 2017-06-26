#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp, Length
from flask_pagedown.fields import PageDownField


class LoginForm(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired()])
    password = PasswordField(label='密码', validators=[DataRequired()])
    submit = SubmitField(label='提交')

class RegistrationForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(u'用户名', validators=[DataRequired(),
                                               Length(1, 64),
                                               Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u'用户名必须由字母、数字、下划线或.组成')])
    password = PasswordField(u'密码', validators=[DataRequired(), EqualTo('password2', message='密码必须一致')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'马上注册')

class PostForm(FlaskForm):
    title = StringField(label=u'标题', validators=[DataRequired()])
    body = PageDownField(label=u'正文', validators=[DataRequired()])
    submit = SubmitField(u'发表')

class CommentForm(FlaskForm):
    body = PageDownField(label=u'评论', validators=[DataRequired()])
    submit = SubmitField(u'发表')