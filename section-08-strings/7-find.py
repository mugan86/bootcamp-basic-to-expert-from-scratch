txt = "Hola, buenas tardes estamos estudiando el curso de Python"

# Valores por defecto (búsqueda solo)
a = txt.find("Hola, ") # 0

a = txt.find("tardes ") # 13

a = txt.find("Hol, ") # -1

# Añadiendo posición inicial desde que empieza a buscar

a = txt.find("Hola, ", 13) # -1

a = txt.find("tardes ", 10) # 13

a = txt.find("Python", -9) # 51

# Añadiendo posición inicial / final

a = txt.find("Hola, ", 0, 3) # -1

a = txt.find("Hol", 0, 3) # 0

a = txt.find("tardes ", 10, 15) # -1

a = txt.find("curso de", -19, -5) # 0 >

print("Final")