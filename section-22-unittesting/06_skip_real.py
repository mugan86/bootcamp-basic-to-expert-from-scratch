import platform
from unittest import main, TestCase, skip, skipIf, skipUnless

"""
print(platform.system()) # Darwin
print(platform.platform()) # macOS-10.15.7-x86_64-i386-64bit
print(platform.architecture()) # ('64bit', '')
print(platform.python_version()) # 3.9.1
"""


class TestExample(TestCase):

    @skipIf(platform.system() == "Darwin", "Ignoramos si no es Darwin.")
    def test_two_if(self):
        print ("Ejecutando sistemas No Darwin")

    @skipIf(platform.system() == "Windows", "Ignoramos porque estamos trabajando con skip")
    def test_three_if(self):
        print("Funciones compatibles con sistemas operativos que no son WINDOWS")


if __name__ == "__main__":
    main()

