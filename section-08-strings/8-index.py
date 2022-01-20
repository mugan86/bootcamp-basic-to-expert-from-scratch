txt = "Hola, buenas tardes estamos estudiando el curso de Python"

# Valores por defecto (búsqueda solo)
a = txt.index("Hola, ") # 0

a = txt.index("tardes ") # 13

# a = txt.index("Hol, ") # ERROR!!!!

# Añadiendo posición inicial desde que empieza a buscar

# a = txt.index("Hola, ", 13) # ERROR!!!!!!

a = txt.index("tardes ", 10) # 13

a = txt.index("Python", -9) # 51

# Añadiendo posición inicial / final

# a = txt.index("Hola, ", 0, 3) # ERROR

a = txt.index("Hol", 0, 3) # 0

a = txt.index("curso de", -19, -5) # 0 >

# a = txt.index("tardes ", 10, 15) # ERROR!!!

print("Final")