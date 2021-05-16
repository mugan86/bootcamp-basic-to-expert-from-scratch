"""
Obtener una lista sin duplicados. Eliminar los que ya existan, para tener una 
lista vacia de valores repetidos (no se puede hacer uso de set que lo veremos 
más tarde).

"""
list = [167, 'Anartz', 4, 4, 4, 5]

res = []
for i in list:
    # Usamos el operador de pertenencia y si no está en la lista final añadimos
    if i not in res:
        res.append(i)

print(f"Lista original: {list}")
print(f"Lista sin duplicados: {res}")