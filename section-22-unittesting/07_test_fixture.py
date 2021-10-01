from unittest import main, TestCase

def square(element):
    return element * element

def execute_assertion(self):
    print("Realizando la aserción")
    result = list(map(square, self.numbers))
    self.assertEqual(
        result,
        [1, 4, 9, 16, 25, 36]
    )

class TestFixture(TestCase):

    def setUp(self):
        print("\nInicializando valores")
        self.numbers = [1, 2, 3, 4, 5, 6]
        
    def test_one(self):
        execute_assertion(self)
        self.numbers.clear()
        print(self.numbers)

    def test_two(self):
        execute_assertion(self)

    def tearDown(self):
        print("Finalizando prueba actual")
        print(self.numbers)
        del(self.numbers)

if __name__ == "__main__":
    main()