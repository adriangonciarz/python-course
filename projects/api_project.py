import json
from pprint import pprint
from faker import Faker

import requests

base = 'https://jsonplaceholder.typicode.com'
posts_uri = f'{base}/posts'
fake = Faker('pl_PL')


def get_posts_list():
    return requests.get(posts_uri).json()


def serialize_json():
    body = {
        "userId": 1,
        "title": fake.bs(),
        "body": fake.sentence(),
        'none_field': None,
        'bool_field': True
    }
    s = json.dumps(body)
    print(s)


def deserialize_json():
    s = '{"userId": 4,"id": 33,"title": "qui explicabo molestiae dolorem","body": "rerum ut et numquam laborum odit est sit id qui sint in quasi tenetur tempore aperiam et quaerat qui in rerum officiis sequi cumque quod"}'
    js = json.loads(s)
    print(js['title'])


def create_new_post():
    body = {
        "userId": 1,
        "title": fake.bs(),
        "body": fake.sentence()
    }
    response = requests.post(posts_uri, json=body)
    print(response.headers['content-type'])
    print(response.status_code)
    print(response.json())


def get_post_with_id(post_id):
    url = f'{posts_uri}/{post_id}'
    return requests.get(url).json()


def delete_post_with_id(post_id):
    url = f'{posts_uri}/{post_id}'
    r = requests.delete(url)
    assert r.status_code == 200


def find_post_with_title(posts, title):
    return next((p for p in posts if p['title'] == title), None)


if __name__ == '__main__':
    posts = get_posts_list()
    posts_titles = [p['title'] for p in posts]
    # pprint(posts_titles)
    # pprint(posts[0:5])
    # serialize_json()
    # deserialize_json()
    # create_new_post()
    # post_33 = get_post_with_id(33)
    # print(post_33)
    p = find_post_with_title(posts, "quam voluptatibus rerum veritatis")
    print(p)