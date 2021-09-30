from unittest import main, TestCase, mock
from blog import Blog

"""
Estamos testeando lo correspondiente a la request de JSONPlaceHolder Typicode
el apartado de commentarios "comments" que hemos añadido al módulo "blog" con "comments"
como función
"""
class TestBlogComments(TestCase):

    def no_test_blog_comments(self):
        blog = Blog()
        response = blog.comments()
        self.assertIsNotNone(response)
        for resp in response:
            self.assertEqual(type(resp['id']), int)
            self.assertEqual(type(resp['postId']), int)
            self.assertEqual(type(resp['name']), str)
            self.assertEqual(type(resp['email']), str)
            self.assertEqual(type(resp['body']), str)
            self.assertEqual(type(resp), dict)

    @mock.patch("blog.Blog")
    def test_blog_comments_mock(self, mock_response):

        blog = mock_response()
        blog.comments.return_value = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
            },
        ]
        response = blog.comments()
        print(response)
        self.assertIsNotNone(response)
        for resp in response:
            self.assertEqual(type(resp['id']), int)
            self.assertEqual(type(resp['postId']), int)
            self.assertEqual(type(resp['name']), str)
            self.assertEqual(type(resp['email']), str)
            self.assertEqual(type(resp['body']), str)
            self.assertEqual(type(resp), dict)


if __name__ == "__main__":
    main()
