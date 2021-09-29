from unittest import main, TestCase
from posts import get_posts

class TestGetPosts(TestCase):
    def test_get_posts(self):
        response = get_posts()

        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    main()