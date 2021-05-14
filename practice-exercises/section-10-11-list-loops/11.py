"""
Hacemos lo mismo que en el 9, pero en vez de sumar, multiplicamos.
"""
total = 1
input_values_correct = False
"""
Aquí vamos a controlar que introducimos el número de elementos
correcto, para luego pedir las veces especificadas para la multiplicación
total de lo que queremos conseguir
"""
while(input_values_correct == False):
    elements = int(input("¿Cuántos números introduciremos? "))
    if (elements < 1): print("Hay que introducir 1 ó más")
    else : input_values_correct = True

counter = 0
"""
Vamos pidiendo lo necesario
"""
while (counter < elements):
    total *= int(input(f"Introduce el número {counter + 1}: "))
    counter += 1

print(f"La multiplicación total de {elements} números: {total}")