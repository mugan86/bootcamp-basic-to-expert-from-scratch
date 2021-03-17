my_dict = {
    'name': 'Anartz Mugika Ledo',
    'email': 'mugan86@gmail.com',
    'languages': ["Euskera", "Español", "Inglés"]
}

# Acceder al nombre
select = my_dict['name']        # 'Anartz Mugika Ledo'
select = my_dict['email']       # 'mugan86@gmail.com'
select = my_dict['languages'] 
# ["Euskera", "Español", "Inglés"]
select = select[-3] # Euskera

select = my_dict.get('name')        # 'Anartz Mugika Ledo'
select = my_dict.get('email')       # 'mugan86@gmail.com'
select = my_dict.get('languages') 
select = my_dict.get('languages_')
# ["Euskera", "Español", "Inglés"]


# Acceder a los valores y claves
# claves
key_values = my_dict.keys()
values = my_dict.values()

# Comprobar si clave existe en un diccionario (Pertenencia)
select = "price" not in my_dict     # True
select = "name" not in my_dict      # False
select = "name" in my_dict          # True
select = "languages" not in my_dict # False
select = "languages" in my_dict     # True
select = "skills" not in my_dict    # True
select = "age" in my_dict           # False

print("FINAL")