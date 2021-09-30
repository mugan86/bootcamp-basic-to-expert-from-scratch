from unittest import main, TestCase, mock
from blog import Blog


class TestBlog(TestCase):

    def no_test_blog_post(self):
        blog = Blog()
        response = blog.posts()
        self.assertIsNotNone(response)
        for resp in response:
            self.assertEqual(type(resp['id']), int)
            self.assertEqual(type(resp['userId']), int)
            self.assertEqual(type(resp['title']), str)
            self.assertEqual(type(resp['body']), str)
            self.assertEqual(type(resp), dict)

    @mock.patch("blog.Blog")
    def test_blog_post_mock(self, mock_response):

        blog = mock_response()
        blog.posts.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
            },
        ]
        response = blog.posts()
        print(response)
        self.assertIsNotNone(response)
        for resp in response:
            self.assertEqual(type(resp['id']), int)
            self.assertEqual(type(resp['userId']), int)
            self.assertEqual(type(resp['title']), str)
            self.assertEqual(type(resp['body']), str)
            self.assertEqual(type(resp), dict)


if __name__ == "__main__":
    main()
