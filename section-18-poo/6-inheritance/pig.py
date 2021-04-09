from animal import Animal

class Pig(Animal):

    def __init__(self, name=None, chip_number=None,
                 genre=None, day_birth=None, 
                 farm = True):
        super().__init__(name, chip_number, genre, day_birth)
        print("Constructor Clase Hija - Cerdo")
        self.__farm = farm
    
    def __del__(self):
        print("Destructor Clase Hija - Cerdo")
    
    def __str__(self):
        print("Detalles del cerdo")

    def take_sunny(self):
        print("Cerdo tomando el sol")
    
    def investigate_environment(self):
        print("Cenrdo investigando el entorno")
    
    def show_details(self):
        super().show_details()
        print("¿Vive en la granja?: {}".format(self.__farm))
        print("===========================")
    
    def talk(self):
        print("Cerdo cuyo nombre es {} está gritando".format(
            self.get_name()
        ))

    def run(self):
        print("Cerdo cuyo nombre es {} está andando".format(
            self.get_name()
        ))

    def eat(self):
        print("Cerdo cuyo nombre es {} está comiendo frutos secos".format(
            self.get_name()
        ))
    
    # setter

    def set_farm(self, farm):
        self.__farm = farm
    
    # getter

    def get_farm(self):
        return self.__farm
