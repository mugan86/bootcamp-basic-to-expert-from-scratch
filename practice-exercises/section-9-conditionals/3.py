"""
Vamos a crear un programa, donde introducimos un número ENTERO y 
debemos de decir si es POSITIVO, NEGATIVO ó NEUTRO (igual a 0).
Datos de prueba:
Introduce el número: -373
Resultado esperado: -373 es NEGATIVO

Introduce el número: 6
Resultado esperado: 6 es POSITIVO.


"""

number_val = int(input("Introduce el número: \n"))


if (number_val < 0): result = "NEGATIVO"
elif (number_val > 0): result = "POSITIVO"
else: result = "NEUTRO"

print(f"{number_val} es {result}")