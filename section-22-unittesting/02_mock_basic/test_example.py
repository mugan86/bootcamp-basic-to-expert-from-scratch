from unittest import main, TestCase, mock
from mock_example import hello
class TestExample(TestCase):
    @mock.patch("mock_example.get_greeting")
    def test_get_hello_text(self, mock_response):
        # Ya hemos mockeado y el contenido "Hola Mundo en el curso de Python" ya no existe
        print(hello())
        mock_response.return_value = "Bienvenid@s al curso de Python"
        print(hello())
        response = hello()
        self.assertEqual(response, "Bienvenid@s al curso de Python")
        self.assertNotEqual(response, "Hola Mundo en el curso de Python")

if __name__ == "__main__":
    main()