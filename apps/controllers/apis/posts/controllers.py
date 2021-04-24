# -*- coding: utf-8 -*-
from flask import Blueprint, request
from flask_login import current_user
from uuid import uuid4

from sqlalchemy import or_

from apps.common.auth import api_signin_required
from apps.common.response import ok, error
from apps.database.models import Post, Tag, Comment, View
from apps.database.session import db
from config import Config

app = Blueprint('apis_posts', __name__, url_prefix='/apis/posts')


@app.route('', methods=['GET'])
@api_signin_required
def get_posts():
    args = request.args
    if args.get('q'):
        search = '%{}%'.format(args['q'])
        posts = Post.query.join(Tag).filter(or_(Post.title.like(search), Post.content.like(search), Tag.title == args['q'])).all()
    else:
        posts = Post.query.all()
    return ok([dict(id=post.id, title=post.title, created_at=str(post.created_at)) for post in posts])


@app.route('', methods=['POST'])
@api_signin_required
def create_post():
    form = request.form
    title = form['title']
    content = form['content']
    tags = form['tags']

    post = Post(title=title, content=content, user_id=current_user.id, tags=[Tag(title=tag) for tag in tags.split(',')])
    db.session.add(post)
    db.session.commit()
    return ok()


@app.route('/<int:post_id>', methods=['PUT'])
@api_signin_required
def update_post(post_id):
    form = request.form
    title = form['title']
    content = form['content']
    tags = form['tags']

    post = Post.query.filter(Post.id == post_id).first()
    if not post:
        return error(40400)
    if current_user.id != post.user_id:
        return error(40300)

    Tag.query.filter(Tag.post_id == post_id).delete()

    post.title = title
    post.content = content
    post.tags = [Tag(title=tag) for tag in tags.split(',')]
    db.session.commit()
    return ok()


@app.route('/<int:post_id>', methods=['DELETE'])
@api_signin_required
def delete_post(post_id):
    post = Post.query.filter(Post.id == post_id).first()
    if not post:
        return error(40400)
    if current_user.id != post.user_id:
        return error(40300)

    Tag.query.filter(Tag.post_id == post_id).delete()
    View.query.filter(View.post_id == post_id).delete()
    Comment.query.filter(Comment.post_id == post_id).delete()
    db.session.delete(post)
    db.session.commit()
    return ok()


@app.route('/file_upload', methods=['POST'])
@api_signin_required
def file_upload():
    args = request.args
    CKEditorFuncNum = args['CKEditorFuncNum']
    upload = request.files['upload']

    random_uuid = uuid4()
    ex = upload.filename.split('.')[1]
    upload.save('{}/media/{}.{}'.format(Config.STATIC_DIR, random_uuid, ex))
    path = '/static/media/{}.{}'.format(random_uuid, ex)
    result = '<script>window.parent.CKEDITOR.tools.callFunction("{}", "{}", "")</script>'.format(
        CKEditorFuncNum, path)
    return result


@app.route('/<int:post_id>/comments/<int:comment_id>', methods=['PUT'])
@api_signin_required
def update_comment(post_id, comment_id):
    data = request.form
    content = data['content']

    post = Post.query.filter(Post.id == post_id).first()
    if not post:
        return error(40400)

    comment = Comment.query.filter(Comment.id == comment_id).first()
    if comment.user_id != current_user.id:
        return error(40300)

    comment.content = content
    db.session.commit()
    return ok()


@app.route('/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
@api_signin_required
def delete_comment(post_id, comment_id):
    post = Post.query.filter(Post.id == post_id).first()
    if not post:
        return error(40400)

    comment = Comment.query.filter(Comment.id == comment_id).first()
    if comment.user_id != current_user.id:
        return error(40300)

    db.session.delete(comment)
    db.session.commit()
    return ok()


@app.route('/<int:post_id>/comments', methods=['POST'])
@api_signin_required
def create_comment(post_id):
    data = request.form
    content = data['content']
    parent_id = data.get('parent_id')

    post = Post.query.filter(Post.id == post_id).first()
    if not post:
        return error(40400)

    comment = Comment(content=content, post_id=post.id, user_id=current_user.id, parent_id=parent_id)
    db.session.add(comment)
    db.session.commit()
    return ok()
