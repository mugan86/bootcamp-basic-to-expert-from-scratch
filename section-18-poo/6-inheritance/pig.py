from animal import Animal

class Pig(Animal):

    def __init__(self, farm):
        print("Constructor Clase Hija - Cerdo")
        self.farm = farm
    
    def __del__(self):
        print("Destructor Clase Hija - Cerdo")
    
    def __str__(self):
        print("Detalles del cerdo")

    def take_sunny(self):
        print("Cerdo tomando el sol")
    
    def investigate_environment(self):
        print("Cenrdo investigando el entorno")