import requests

POST_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    response = requests.get(POST_URL)

    if response.ok:
        return response
    else:
        return None