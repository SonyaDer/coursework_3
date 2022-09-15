from flask import Blueprint, jsonify, abort
import logging

from app.dao.main_dao import get_posts_all, get_post_by_pk

app_api = Blueprint('app_api', __name__)

api_logger = logging.getlogger('api_logger')

@app_api.route('/')
def app_posts_hi():
    api_logger.debug('Начальная страница')
    return 'Hello in API ;P Эндпоинты api/posts, api/post/<post_id>'

@app_api.route('/posts/')
def app_posts_all():
    try:
        posts = get_posts_all()
    except:
        return abort(404)
    api_logger.debug('Запрошены все посты')
    return jsonify(posts)

@app_api.route('/post/<int:post_id>/')
def app_posts_single(post_id: int):
    post_pk = get_post_by_pk(post_id)
    api_logger.debug('Запрошен пост')
    return jsonify(post_pk)