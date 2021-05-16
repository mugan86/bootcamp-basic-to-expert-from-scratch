"""
Escribe un programa que haga nos diga cual es el número superior de una lista dada.
Solo introducir números.

"""

list_values = [178293, 93902, 2819, -120293939]
max_value = list_values[0]

for value in range(1, len(list_values)):
    if (max_value <= list_values[value]): max_value = list_values[value]

print(f"El mayor de la lista: {list_values}")
print(f"======> {max_value}")