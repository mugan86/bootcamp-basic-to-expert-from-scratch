# Añadimos el template / clase generica
class SportInfo:
    """Mostrar información de un deporte"""
    name = ""

# Añadimos los objetos asociados a esa clase
run = SportInfo()
run.name = "Correr"
print(run.name) # Correr
print(run.__doc__)

swim = SportInfo()
swim.name = "Nadar"
print(swim.name) # ""
print(swim.__doc__)

print("Final")
