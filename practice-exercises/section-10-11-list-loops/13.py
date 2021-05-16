"""
Escribe un programa que haga nos diga cual es el número inferior 
de una lista dada.

Solo introducir números.

"""

list_values = [178293, 93902, 2819, -120293939]

min_value = list_values[0]

for value in range(1, len(list_values)):
    if (min_value > list_values[value]): min_value = list_values[value]

print(f"El menor de la lista: {list_values}")
print(f"======> {min_value}")