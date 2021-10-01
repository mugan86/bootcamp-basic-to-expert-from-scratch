from unittest import main, TestCase, skip, skipIf, skipUnless

class TestExample(TestCase):
    @skip("Ignoramos porque estamos trabajando con skip")
    def test_one(self):
        print("Test one")

    @skipIf(10 == 10, "Ignoramos porque estamos trabajando con skip")
    def test_two_if(self):
        print ("10 == 10 - skipIf")

    @skipIf(10 > 10, "Ignoramos porque estamos trabajando con skip")
    def test_three_if(self):
        print("10 > 10 - skipIf")

    @skipUnless(10 == 10, "Ignoramos porque estamos trabajando con skip")
    def test_two_unless(self):
        print ("10 == 10 - skipUnless")

    @skipUnless(10 > 10, "Ignoramos porque estamos trabajando con skip")
    def test_three_unless(self):
        print("10 > 10 - skipUnless")

if __name__ == "__main__":
    main()