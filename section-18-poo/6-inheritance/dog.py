from animal import Animal


class Dog(Animal):

    def __init__(self, name=None, chip_number=None,
                 genre=None, day_birth=None,
                 address=""):
        super().__init__(name, chip_number, genre, day_birth)
        print("Constructor Clase Hija - Perro")
        self.address = address

    def __del__(self):
        print("Destructor Clase Hija - Perro")

    def __str__(self):
        print("Detalles del perro")

    def clean(self):
        print("Limpiando al perro")

    def show_details(self):
        super().show_details()
        print("Domicilio: {}".format(self.address))
        print("===========================")
    
    def talk(self):
        print("Perro cuyo nombre es {} está ladrando".format(
            self.name
        ))

    def run(self):
        print("Perro cuyo nombre es {} está corriendo".format(
            self.name
        ))

    def eat(self):
        print("Perro cuyo nombre es {} está comiendo un hueso".format(
            self.name
        ))
