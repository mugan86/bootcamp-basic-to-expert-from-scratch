my_dict = {
    'name': 'Anartz Mugika Ledo',
    'email': 'mugan86@gmail.com',
    'languages': ["Euskera", "Español", "Inglés"],
    'age': 35,
    'town': 'Soraluze (Gipuzkoa)'
}

copy_one = my_dict.copy()

# Modificar información
copy_one['name'] = "-----"
copy_one['email'] = "........"
copy_one.pop('languages')
copy_one.popitem()
copy_one.update({'town': 'Bergara (Gipuzkoa)'})

copy_one = dict(my_dict)

# Modificar información
copy_one['name'] = "3939393939933"
copy_one['email'] = 333333
copy_one.pop('town')
copy_one.popitem() # age
copy_one.update({'town': 'Eibar (Gipuzkoa)'})

print("FINAL")