from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    confirm_password = PasswordField('パスワード確認', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('登録')

class LoginForm(FlaskForm):
    email = StringField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    submit = SubmitField('ログイン')

class PostForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
    submit = SubmitField('投稿')

class CommentForm(FlaskForm):
    content = TextAreaField('コメント', validators=[DataRequired()])
    submit = SubmitField('コメント')
