"""
Escribe un programa que haga cuente cuantas veces aparece un número en una tupla que añadiremos
de manera DINÁMICA, ya que puede cambiar el valor de entrada.
Guardarla en una tupla de este estilo:
((número-buscado, apariciones), (número-buscado, apariciones), (número-buscado, apariciones))
Usando un ejemplo real:
Entrada: (2, 3, 4, 4, 5, 5, 6, 2, 2, 2, 2)
Salida: ((2, 5), (3, 1), (4, 2), (5, 2))
"""

tuple_list = (2, 3, 4, 4, 5, 5, 6, 2, 2, 2, 2)
list_diff_numbers = []
list_with_counts = []

for item in tuple_list:
    if (list_diff_numbers.count(item) == 0):
        # El número no analizado cuantas veces aparece
        list_with_counts.append([item, tuple_list.count(item)])
        # Almacenamos el número para que no evalue de nuevo
        list_diff_numbers.append(item)

print(f'Resultado final: {tuple(list_with_counts)}')
