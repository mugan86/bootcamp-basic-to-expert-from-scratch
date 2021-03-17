my_dict = {
    'name': 'Anartz Mugika Ledo',
    'email': 'mugan86@gmail.com',
    'languages': ["Euskera", "Español", "Inglés"],
    'age': 35,
    'town': 'Soraluze (Gipuzkoa)'
}

# claves
print("Mostrar los valores clave del diccionario")
for key_value in my_dict:
    print(key_value)
print("---------")
for key_value in my_dict.keys():
    print(key_value)

# valores
print("Mostrar los valores del contenido asociado a las claves")
for key_value in my_dict:
    print(my_dict[key_value])
    print(my_dict.get(key_value))
print("---------")
for value in my_dict.values():
    print(value)

# Items completo
print("Mostrar información completa:")
for key_value, value in my_dict.items():
    print(f"{key_value}:     \t{value}")