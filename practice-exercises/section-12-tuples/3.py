"""
Crear una tupla de 3 números enteros. 
Una vez creada:
Desempaquetamos con “unpack” en 3 variables.
Suma de los 3 valores después de desempaquetar.
Intentamos desempaquetar en 4 variables, ¿Qué ocurre? ¿Funcionará?
"""

numbers_tuple = (1, 2, 3)

# 3 valores
x, y, z = numbers_tuple

total_values = x + y + z

# 4 valores

"""
Error, por tener 3 valores en la tupla y estamos esperando 4 al desempaquetar
x, y, z, a = numbers_tuple
total_values = x + y + z + a
"""