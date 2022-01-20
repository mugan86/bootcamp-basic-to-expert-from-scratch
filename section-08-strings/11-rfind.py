txt = '¿Este es el curso de Python? Si, es el curso Bootcamp de Python'

# Valores por defecto (subcadena de búsqueda)

a = txt.rfind("curso") # 39. Posición que no es 12 (la primera aparición)

a = txt.rfind("python") # -1

a = txt.rfind("Python") # 57. Posición que no es 21 (la primera aparición)

# Añadiendo las selecciones

a = txt.rfind("curso", 30) # 39. Posición que no es 12 (la primera aparición)

a = txt.rfind("Python", 0, 10) # -1

a = txt.rfind("Python", -15, -5) # -1

a = txt.rfind("Bootcamp", -40, -5) # 45

print("Final")