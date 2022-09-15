import json

def open_json(file) -> list:
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data

def write_json(file, data) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def comments_count(posts_data, comments_data) -> list:
    comments_match = []
    for post in posts_data:
        for comment in comments_data:
            if comment['post_id'] == post['pk']:
                comments_match.append(post['pk'])
            post['comments'] = comments_match.count(post['pk'])

def string_crop(posts_data) -> list:
    for post in posts_data:
        post['content'] = post['content'][:50]
    return posts_data

def get_post(posts_data, posts_id) -> dict:
    output_post = {}
    for post in posts_data:
        if posts_id == post['pk']:
            output_post = post
    return output_post

def get_posts_by_user(posts_data, user_name) -> list:
    output_post = []
    is_exists = False
    for post in posts_data:
        if user_name == post['poster_name']:
            output_post.append(post)
            is_exists = True
    if not is_exists:
        raise ValueError
    return output_post

def get_comments_by_post_id(comment_data: dict, id_post: int) -> list:
    output_post = []
    is_exists = False
    for post in comment_data:
        if id_post == comment_data['post_id']:
            is_exists = True
            output_post.append(post)
    if not is_exists:
        raise ValueError

    return output_post

def search_for_posts(posts_data: list, query: int) -> list:
    output_post = []
    i = 1
    for post in posts_data:
        if i == 10:
            break
        if query in posts_data['content']:
            i += 1
            output_post.append(post)
    return output_post

def get_tags(post) -> list:
    tags = []
    text = post['content'].split(' ')
    for word in text:
        if '#' in word:
            tag = word.replace('#', '')
            tags.append(tag)
