from flask import Blueprint, render_template, request

from app.dao.main_dao import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__)

@search_blueprint.route('/search/')
def search_page():
    qwery = request.args.get("s").lower()
    posts = search_for_posts(qwery)
    return render_template('search.html', posts=posts)
