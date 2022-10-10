from flask import Blueprint, render_template

from dao.main_dao import get_posts_all

user_feed_blueprint = Blueprint('user_feed_blueprint', __name__)

@user_feed_blueprint.route('/user-feed/<name>')
def user_feed(name):
    posts = get_posts_all()
    user_posts = []
    for post in posts:
        if post["poster_name"] == name:
            user_posts.append(post)
    return render_template('user-feed.html', user_posts=user_posts, name=name)


