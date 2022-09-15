from flask import Blueprint, render_template

from app.dao.main_dao import get_posts_all

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def index_page():
    return render_template('index.html', all_posts=get_posts_all())