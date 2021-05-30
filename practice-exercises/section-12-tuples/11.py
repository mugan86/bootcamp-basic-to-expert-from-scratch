"""
Copia los elementos que están desde el 44 y el 55 (no incluido) en la tupla, 
creando una nueva tupla. Usamos ínidices positivos y negativos, según las necesidades
tupla = (1, 2, 3, 44, 66, 77, 78, 2, 1, 55, 90, 100)
nueva_tupla = (44, 66, 77, 78, 2, 1)
"""

tuple_list = (1, 2, 3, 44, 66, 77, 78, 2, 1, 55, 90, 100)

new_tuple_list = tuple_list[3:-3]

print(new_tuple_list)