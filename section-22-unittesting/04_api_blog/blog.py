import requests

class Blog:

    def posts(self):
        return requests.get("https://jsonplaceholder.typicode.com/posts").json()

    def comments(self):
        return requests.get("https://jsonplaceholder.typicode.com/comments").json()


"""La prueba del Blog
blog = Blog()

print(blog.posts())"""