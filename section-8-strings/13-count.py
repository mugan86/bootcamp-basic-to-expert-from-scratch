txt = '¿Este es el curso de Python? Si, es el curso Bootcamp de Python'

# Valores por defecto (subcadena de búsqueda)

a = txt.count("Python") # 2

a = txt.count("curso")  # 2

a = txt.count("Curso")  # 0

# Añadiendo las selecciones

a = txt.count("curso", 30)              # 1

a = txt.count("Bootcamp", -40, -5)      # 1

a = txt.count("Bootcamp", -7, -5)       # 0
a = txt.count("Python", -7)             # 1

print("Final")