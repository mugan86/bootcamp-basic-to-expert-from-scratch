my_dict = {
    'name': 'Anartz Mugika Ledo',
    'email': 'mugan86@gmail.com',
    'languages': ["Euskera", "Español", "Inglés"]
}

# Añadir elementos en el diccionario

my_dict['age'] = 35
my_dict.update({'hobbys': ["Deporte", "Estudiar", "Series"]})

# Modificar información en los diccionarios
my_dict['name'] = 'Anartz Mugika Ledo ----->'
my_dict['email'] = 'anartz@mugika.com'

list_languages = list(my_dict['languages'])
list_languages.append("Italiano")
list_languages.append("Alemán")
my_dict['languages'] = list_languages

# Añadimos un nuevo hobby => "Monataña"
list_hobbys = list(my_dict['hobbys'])
list_hobbys.insert(1, "Montaña")
my_dict['hobbys'] = list_hobbys
print("FINAL")