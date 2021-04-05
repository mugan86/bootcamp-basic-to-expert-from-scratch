from animal import Animal

class Cat(Animal):

    def __init__(self, live_in_street):
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