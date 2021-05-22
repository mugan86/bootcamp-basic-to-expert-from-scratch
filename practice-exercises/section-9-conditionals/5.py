"""
Vamos a crear un programa, donde introducimos un número ENTERO que es la edad 
y debemos comprobar is esa persona es mayor de edad y con ello, tiene permitido
votar en las elecciones generales.
Datos de prueba:
Introduce edad: 18
Resultado esperado: Si tiene permitido votar en las elecciones generales.
--------------
Introduce edad: 17
Resultado esperado: NO tiene permitido votar en las elecciones generales.

"""

age = int(input("Introduce edad: \n"))

if (age >= 18):
    print("Si tiene permitido votar en las elecciones generales")
else: print("NO tiene permitido votar en las elecciones generales")
