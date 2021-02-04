txt = '¿Este es el curso de Python? Si, es el curso Bootcamp de Python'

# Valores por defecto (subcadena de búsqueda)

a = txt.rindex("curso") # 39. Posición que no es 12 (la primera aparición)

# a = txt.rindex("python") # ERROR!!!

a = txt.rindex("Python") # 57. Posición que no es 21 (la primera aparición)

# Añadiendo las selecciones

a = txt.rindex("curso", 30) # 39. Posición que no es 12 (la primera aparición)

# a = txt.rindex("Python", 0, 10) # ERROR!!!

# a = txt.rindex("Python", -15, -5) # ERROR!!!

a = txt.rindex("Bootcamp", -40, -5) # 45

print("Final")