import requests

class Blog:

    def posts(self):
        return requests.get("https://jsonplaceholder.typicode.com/posts").json()


"""La prueba del Blog"""
blog = Blog()

print(blog.posts())