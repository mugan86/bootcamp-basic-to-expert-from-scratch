"""
Crear una tupla de 3 números enteros. 
Una vez creada:
Desempaquetamos con “unpack” en 3 variables.
Suma de los 3 valores después de desempaquetar.
Añadir un nuevo elemento en la tupla. No es posible directamente pero podremos hacerlo.
Intentamos desempaquetar en 4 variables

"""

numbers_tuple = (1, 2, 3)

# 3 valores
x, y, z = numbers_tuple

total_values = x + y + z

# 4 valores
# Añadir un nuevo valor
numbers_list = list(numbers_tuple)
numbers_list.append(45)
numbers_tuple = tuple(numbers_list) 

x, y, z, a = numbers_tuple
total_values = x + y + z + a

# total_values = 51