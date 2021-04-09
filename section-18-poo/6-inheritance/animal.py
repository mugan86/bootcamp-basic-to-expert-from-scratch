class Animal:

    def __init__(self, name, chip_number, genre, day_birth):
        print("Constructor Super clase - Animal")
        if (name == None or chip_number == None or genre == None or
        day_birth == None):
            raise ValueError("Debes de especificar todos los valores")
        self.__name = name
        self.__chip_number = chip_number
        self.__genre = genre
        self.__day_birth = day_birth
    
    def __del__(self):
        print("Destructor Super clase - Animal")
    
    def __str__(self):
        print("Detalles del animal")

    def show_details(self):
        print("===========================")
        print("Detalles del animal")
        print("Nombre: {}".format(self.__name))
        print("Nº Chip: {}".format(self.__chip_number))
        print("Género: {}".format(self.__genre))
        print("Fecha de nacimiento: {}".format(self.__day_birth))
    
    def talk(self):
        print("Animal hablando")
    
    def run(self):
        print("Animal corriendo")

    def eat(self):
        print("Animal comiendo")

    # Setter

    def set_name(self, name):
        self.__name = name
    
    def set_genre(self, genre):
        self.__genre = genre
    
    def set_chip_number(self, chip_number):
        self.__chip_number = chip_number

    def set_day_birth(self, day_birth):
        self.__day_birth = day_birth

    # getter

    def get_name(self):
        return self.__name
    
    def get_genre(self):
        return self.__genre
    
    def get_chip_number(self):
        return self.__chip_number

    def get_day_birth(self):
        return self.__day_birth

    