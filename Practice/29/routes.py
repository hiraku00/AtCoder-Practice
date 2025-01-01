from flask import render_template, redirect, url_for, request, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm, LoginForm, PostForm, CommentForm
from .model import User, Post, Comment  # モデルのインポートを修正
from datetime import datetime
from . import db

auth = Blueprint('auth', __name__, url_prefix='/auth')
main = Blueprint('main', __name__)

# @current_app.login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('登録が完了しました。ログインしてください。', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('ログインに失敗しました。メールアドレスとパスワードを確認してください。', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('投稿が作成されました！', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(content=comment_form.content.data, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('コメントが投稿されました！', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))
    return render_template('view_post.html', title=post.title, post=post, comment_form=comment_form)

@main.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('投稿が更新されました！', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Edit Post', form=form, legend='Edit Post')

@main.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('投稿が削除されました！', 'success')
    return redirect(url_for('main.index'))

@main.route('/comment/edit/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    form = CommentForm()
    if form.validate_on_submit():
        comment.content = form.content.data
        db.session.commit()
        flash('コメントが更新されました！', 'success')
        return redirect(url_for('main.view_post', post_id=comment.post_id))
    elif request.method == 'GET':
        form.content.data = comment.content
    return render_template('edit_comment.html', title='Edit Comment', form=form)

@main.route('/comment/delete/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    post_id = comment.post_id
    db.session.delete(comment)
    db.session.commit()
    flash('コメントが削除されました！', 'success')
    return redirect(url_for('main.view_post', post_id=post_id))
