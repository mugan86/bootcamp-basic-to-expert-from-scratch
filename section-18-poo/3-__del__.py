# Añadimos el template / clase generica
class SportInfo:
    """Mostrar información de un deporte"""

    def __init__(self, name):
        print("Estamos creando un objeto")
        self.name = name

    def __del__(self):
        print("Estamos destruyendo un objeto: {}"
              .format(self.__class__.__name__))


# Añadimos los objetos asociados a esa clase
run = SportInfo("Correr")
print(run.name)  # Correr
print(run.__doc__)
del run 
swim = SportInfo("Nadar")
print(swim.name)  # ""
print(swim.__doc__)
del swim
print("Final")
