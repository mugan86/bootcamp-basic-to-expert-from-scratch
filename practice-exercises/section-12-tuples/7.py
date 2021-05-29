"""
Crear una tupla de “n” elementos y darle la vuelta usando un bucle while y for.
"""

print("===============FOR===============")
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(f'Inicio: {numbers_tuple}')
numbers_list = []
for item in range(len(numbers_tuple), 0, -1):
    numbers_list.append(item)

numbers_tuple = tuple(numbers_list)

print(f'Final: {numbers_tuple}')

print("===============WHILE===============")
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(f'Inicio: {numbers_tuple}')
numbers_list = []
i = len(numbers_tuple) - 1
while(i >= 0):
    numbers_list.append(numbers_tuple[i])
    i -= 1

numbers_tuple = tuple(numbers_list)

print(f'Final: {numbers_tuple}')