d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)

# Destruir d1 y d2
del d1
del d2
print(f"Mezcla: {d}")

# No imprimir, si no da error (descomentando probamos)
"""
print(f"D1: {d1}")
print(f"D2: {d2}")
"""