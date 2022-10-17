import json

def open_json(file) -> list:
    with open(file, 'r', encoding='utf-8') as f:
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

def get_posts_all():
    with open('data/posts.json', 'r', encoding='ut-8') as f:
        return json.load(f)

def get_posts_by_user(user_name):
    posts = get_posts_all()
    return [post for post in posts if post['poster_name'] == user_name]

def get_comments_all():
    with open('data/comments.json', 'r', encoding='ut-8') as f:
        return json.load(f)

def get_comments_by_post_id(post_id):
    comments = get_comments_all()
    return [comment for comment in comments if comment['post_id'] == post_id]

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
