from unittest import main, TestCase, mock
from blog import Blog

class TestBlog(TestCase):

    def test_blog_post(self):
        blog = Blog()
        response = blog.posts()
        self.assertIsNotNone(response)
        for resp in response:
            self.assertEqual(type(resp['id']), int)
            self.assertEqual(type(resp['userId']), int)
            self.assertEqual(type(resp['title']), str)
            self.assertEqual(type(resp['body']), str)
            self.assertEqual(type(resp), dict)

if __name__ == "__main__":
    main()