"""
Crear una tupla de desde la vuestro nombre de pila 
y apellidos y darle la vuelta usando un bucle while y for.
"""

name_lastname_tuple = tuple("anartz mugika ledo")

print("===============FOR===============")
print(f'Inicio: {name_lastname_tuple}')
numbers_list = []
for item in range(len(name_lastname_tuple), 0, -1):
    numbers_list.append(item)

name_lastname_tuple = tuple(numbers_list)

print(f'Final: {name_lastname_tuple}')

print("===============WHILE===============")
name_lastname_tuple = tuple("anartz mugika ledo")
print(f'Inicio: {name_lastname_tuple}')
numbers_list = []
i = len(name_lastname_tuple) - 1
while(i >= 0):
    numbers_list.append(name_lastname_tuple[i])
    i -= 1

name_lastname_tuple = tuple(numbers_list)

print(f'Final: {name_lastname_tuple}')