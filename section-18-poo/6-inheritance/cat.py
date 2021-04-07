from animal import Animal


class Cat(Animal):

    def __init__(self, name=None, chip_number=None,
                 genre=None, day_birth=None,
                 live_in_street=False):
        super().__init__(name, chip_number, genre, day_birth)
        print("Constructor Clase Hija - Gato")
        self.live_in_street = live_in_street

    def __del__(self):
        print("Destructor Clase Hija - Gato")

    def __str__(self):
        print("Detalles del gato")

    def climb(self):
        print("Escalando el gato")

    def jump(self):
        print("Saltando el gato")
    
    def show_details(self):
        super().show_details()
        print("¿Vive en la calle?: {}".format(self.live_in_street))
        print("===========================")

    def talk(self):
        print("Gato cuyo nombre es {} está maullando".format(
            self.name
        ))

    def run(self):
        print("Gato cuyo nombre es {} está corriendo".format(
            self.name
        ))

    def eat(self):
        print("Gato cuyo nombre es {} está comiendo atún".format(
            self.name
        ))
