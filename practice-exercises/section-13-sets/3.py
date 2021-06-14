"""
¿Cuál es la longitud del conjunto?.
3. 4 es un valor qque está duplicado y únicamente dejamos unos
Accedemos al elemento de la posición índice. ¿Qué información aparecerá?
No existen índices, al ser desordenada accedemos mediante un bucle
Recorrer el conjunto elemento a elemento.
"""

# Inicializar
set_values = set((4, 3, 4, 5))

print(f'Longitud: {len(set_values)}')

# Recorrer elementos
for element in set_values:
    print(element)