import unittest


class TestAssertions(unittest.TestCase):

    def test_one(self):
        """
        assertEqual(num1, num2, mensaje de error en el caso de aserción)
        assertNotEqual
        assertTrue
        assertFalse
        """
        self.assertEqual(
            2, 2, "Los valores introducidos son diferentes. Deben de ser iguales")

        self.assertNotEqual(
            3, 2, "Los valores introducidos son iguales. Deben de ser diferentes")

        self.assertTrue(" ", "En este caso debe de ser verdadero y es falso")
        self.assertTrue(-1223, "En este caso debe de ser verdadero y es falso")
        self.assertTrue(1, "En este caso debe de ser verdadero y es falso")
        self.assertTrue(True, "En este caso debe de ser verdadero y es falso")

        self.assertFalse("", "En este caso debe de ser falso y es verdadero")
        self.assertFalse(0, "En este caso debe de ser falso y es verdadero")
        self.assertFalse(
            False, "En este caso debe de ser falso y es verdadero")

    def test_two(self):
        """
        assertIs
        assertIsNot
        assertIsNone
        assertIsNotNone
        """

        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = list1

        self.assertIs(
            list1, list3, "No son iguales, no ocupan la misma posicción de memoria")
        self.assertIsNot(
            list1, list2, "Son iguales, ocupan la misma posicción de memoria")

        a = None
        self.assertIsNone(a)
        a = 11
        self.assertIsNotNone(a)

    def test_three(self):
        list_values = [1, 2, 3]
        name = "anartz"

        self.assertIn(1, list_values, "El elemento no se encuentra, tiene que estar en la lista")
        self.assertIn("a", name, "El elemento no se encuentra, tiene que estar en la cadena de texto")

        self.assertNotIn(-1, list_values, "El elemento se encuentra dentro de la lista. No debe de encontrarse")
        self.assertNotIn("o", name, "El elemento se encuentra, no tiene que estar en la cadena de texto")

if __name__ == "__main__":
    unittest.main()
