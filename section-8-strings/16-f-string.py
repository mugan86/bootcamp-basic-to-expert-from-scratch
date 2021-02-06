# Haciendo uso de f-string

# Añadiendo variables interpolando dentro del string
course = "Python"
name = "Anartz Mugika Ledo"
a = f'Nombre del curso: {course}. Instructor: {name}'
# Nombre del curso: Python. Instructor: Anartz Mugika Ledo

# Expresiones dentro de las interpolaciones
a = f'{ 12 + 12 + 4 + 5}' # 33
a = f'{ 12 + 12 * (4 + 5)}' # 120

a = f'{name.lower()}' # anartz mugika ledo
a = f'{name.title()}' # Anartz Mugika Ledo
a = f'{name.capitalize()}' # Anartz mugika ledo

# Usando caracteres de escape

a = f'Hola soy \'{name}\'.\t Estoy enseñando el curso {course}.'
# Hola soy 'Anartz Mugika Ledo'.    Estoy enseñando el curso Python.
print(a)