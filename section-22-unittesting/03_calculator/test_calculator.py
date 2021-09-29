from unittest import main, TestCase, mock
from calculator import Calculator

class TestCalculator(TestCase):
    @mock.patch.object(Calculator, "add")
    def test_add(self, mock_response):
        mock_response.return_value = 230
        calculator = Calculator()
        result = calculator.add(12 , 14)
        print(result)
        self.assertEqual(result, 230)

if __name__ == "__main__":
    main()