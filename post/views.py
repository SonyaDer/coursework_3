from flask import Blueprint, render_template

from dao.main_dao import get_post_by_pk, get_comments_by_post_id

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.route('/post/<int:post_id>', methods=["GET", "POST"])
def post_page(post_id: int):
    post_by_id = get_post_by_pk(post_id)
    if not post_by_id:
        return "<span class='item__username'>Пост отсутствует</span>"
    else:
        get_comments_by_post_id(post_id)
        return render_template('post.html', post_by_id=post_by_id, comments=get_comments_by_post_id(post_id))

