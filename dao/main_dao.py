import json

def get_posts_all():
    with open('data/data.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_posts_by_user(user_name):
    result = []
    for post in get_posts_all():
        if user_name.lower() in post['poster_name'].lower():
            result.append(post)
    return result

def get_comments_all():
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_comments_by_post_id(post_id):
    result = []
    for comments in get_comments_all():
        if post_id == comments['post_id']:
            result.append(comments)
    return result

def search_for_posts(query):
    result = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result

def get_post_by_pk(pk) -> dict:
    all_posts = get_posts_all()
    return all_posts[int(pk) - 1]
