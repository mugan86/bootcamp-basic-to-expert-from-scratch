from animal import Animal


class Dog(Animal):

    def __init__(self, name=None, chip_number=None,
                 genre=None, day_birth=None,
                 address=""):
        super().__init__(name, chip_number, genre, day_birth)
        print("Constructor Clase Hija - Perro")
        self.__address = address

    def __del__(self):
        print("Destructor Clase Hija - Perro")

    def __str__(self):
        print("Detalles del perro")

    def clean(self):
        print("Limpiando al perro")

    def show_details(self):
        super().show_details()
        print("Domicilio: {}".format(self.__address))
        print("===========================")
    
    def talk(self):
        print("Perro cuyo nombre es {} está ladrando".format(
            self.get_name()
        ))

    def run(self):
        print("Perro cuyo nombre es {} está corriendo".format(
            self.get_name()
        ))

    def eat(self):
        print("Perro cuyo nombre es {} está comiendo un hueso".format(
            self.get_name()
        ))
    
    # setter

    def set_address(self, address):
        self.__address = address
    
    # getter

    def get_address(self):
        return self.__address