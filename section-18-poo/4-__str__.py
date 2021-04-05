# Añadimos el template / clase generica
class SportInfo:
    """Mostrar información de un deporte"""

    def __init__(self, name):
        print("Estamos creando un objeto")
        self.name = name

    def __del__(self):
        print("Estamos destruyendo un objeto: {}"
              .format(self.__class__.__name__))

    def __str__(self):
         return "Deporte seleccionado: {}".format(self.name)


# Añadimos los objetos asociados a esa clase
run = SportInfo("Correr")
print(run)  # Deporte seleccionado: Correr
print(run.__doc__)
del run 
swim = SportInfo("Nadar")
print(swim)  # "Deporte seleccionado: Nadar"
print(swim.__doc__)
del swim
print("Final")
