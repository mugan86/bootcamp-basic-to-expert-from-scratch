from animal import Animal 
class Dog(Animal):

    def __init__(self, name, chip_number, genre, day_birth, address):
        super().__init__(name, chip_number, genre, day_birth)
        print("Constructor Clase Hija - Perro")
        self.address = address
    
    def __del__(self):
        print("Destructor Clase Hija - Perro")
    
    def __str__(self):
        print("Detalles del perro")

    def clean(self):
        print("Limpiando al perro")