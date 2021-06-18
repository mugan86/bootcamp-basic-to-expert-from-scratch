dictionary = {'c1': 'Rojo', 'c2': 'Verde', 'c3': None,
    'anartz': None, 'valor': 1, 'ultimo': None}

print(f"Diccionario Inicial: {dictionary}")

# Crear un diccionario provisional que iremos modificando
# Esto se realiza, porque si vamos eliminando en un iterable 
# que usamos en un for, nos salta un error.
prov_dict = dictionary.copy()
for key, value in dictionary.items():
    if (value == None):
        prov_dict.pop(key)
        
# Asignar el resultado en el diccionario original
dictionary = prov_dict
print(f"Diccionario Final: {dictionary}")
