# Añadimos el template / clase generica
class SportInfo:
    """Mostrar información de un deporte"""
    def __init__(self, name):
        print("Estamos creando un objeto")
        self.name = name

# Añadimos los objetos asociados a esa clase
run = SportInfo("Correr")
print(run.name) # Correr
print(run.__doc__)

swim = SportInfo("Nadar")
print(swim.name) # ""
print(swim.__doc__)

print("Final")
