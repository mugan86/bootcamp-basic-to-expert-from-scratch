# Inicializar diccionarios
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

# Copiamos el primer diccionario por ejemplo
d = d1.copy()

# Añadimos el segundo a la copia del nuevo diccionario y mezclamos
d.update(d2)
print(f"Mezcla: {d}")
print(f"D1: {d1}")
print(f"D2: {d2}")