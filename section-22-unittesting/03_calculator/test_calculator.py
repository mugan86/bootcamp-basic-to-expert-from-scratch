from unittest import main, TestCase, mock
from calculator import Calculator

class TestCalculator(TestCase):
    @mock.patch.object(Calculator, "add")
    def test_add(self, mock_response):
        mock_response.return_value = 110
        calculator = Calculator()
        result = calculator.add(12 , 14)
        print(result)
        self.assertEqual(result, 110)

    def test_add_not_mock(self):
        calculator = Calculator()
        result = calculator.add(12 , 14)
        print(result)
        self.assertEqual(result, 26)
        result = calculator.add(11 , 14)
        print(result)
        self.assertEqual(result, 25)
        result = calculator.add(10 , 14)
        print(result)
        self.assertNotEqual(result, 26)

if __name__ == "__main__":
    main()