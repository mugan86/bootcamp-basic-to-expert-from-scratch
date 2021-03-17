my_dict = {
    'name': 'Anartz Mugika Ledo',
    'email': 'mugan86@gmail.com',
    'languages': ["Euskera", "Español", "Inglés"],
    'age': 35,
    'town': 'Soraluze (Gipuzkoa)'
}

delete = my_dict.pop('town') # 'Soraluze (Gipuzkoa)'

delete = my_dict.popitem() # 'age': 35

# Eliminar todos los elementos
my_dict.clear() # 0 elementos
my_dict['name'] = 'Anartz Mugika Ledo' # 1

del my_dict
my_dict = { 'age': 35 }
my_dict['name'] = 'Anartz Mugika Ledo' # 1
print("FINAL")

