class Animal:

    def __init__(self, name, chip_number, genre, day_birth):
        print("Constructor Super clase - Animal")
        if (name == None or chip_number == None or genre == None or
        day_birth == None):
            raise ValueError("Debes de especificar todos los valores")
        self.name = name
        self.chip_number = chip_number
        self.genre = genre
        self.day_birth = day_birth
    
    def __del__(self):
        print("Destructor Super clase - Animal")
    
    def __str__(self):
        print("Detalles del animal")

    def show_details(self):
        print("===========================")
        print("Detalles del animal")
        print("Nombre: {}".format(self.name))
        print("Nº Chip: {}".format(self.chip_number))
        print("Género: {}".format(self.genre))
        print("Fecha de nacimiento: {}".format(self.day_birth))
    
    def talk(self):
        print("Animal hablando")
    
    def run(self):
        print("Animal corriendo")

    def eat(self):
        print("Animal comiendo")

    