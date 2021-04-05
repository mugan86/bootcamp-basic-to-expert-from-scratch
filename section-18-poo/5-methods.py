# Añadimos el template / clase generica
class SportInfo:
    """Mostrar información de un deporte"""

    def __init__(self, name, team):
        print("Estamos creando un objeto")
        self.name = name
        self.team = team

    def __del__(self):
        print("Estamos destruyendo un objeto: {}"
              .format(self.__class__.__name__))

    def __str__(self):
        return "Deporte seleccionado: {}".format(self.name)

    def train(self):
        print("Estamos entrenando en {}".format(self.name))

    def show_details(self):
        print("DEPORTE:")
        print("Nombre: {}".format(self.name))
        print("Deporte de equipo: {}".format(self.team))


# Añadimos los objetos asociados a esa clase
run = SportInfo("Correr", False)
print(run)  # Deporte seleccionado: Correr
run.train()
run.show_details()
del run
swim = SportInfo("Nadar", True)
print(swim)  # "Deporte seleccionado: Nadar"
swim.train()
swim.show_details()
del swim
print("Final")
