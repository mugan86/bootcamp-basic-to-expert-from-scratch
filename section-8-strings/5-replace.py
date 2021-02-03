# Reemplazar una subcadena dentro de la cadena de texto

str_content = "Hola al curso de Python con Anartz Mugika"

a = str_content.replace("Hola", "Adios") # "Adios al curso de ..."
a = str_content.replace("Anartz Mugika", "ustedes") # "Hola ... con ustedes"
str_content = "Hola al curso de _Python con Anartz Mugika____"
a = str_content.replace("_", "") # "Hola ... con ustedes"

# Reemplazamos solo 2 veces
a = str_content.replace("_", "", 2) # "Hola al curso de Python con Anartz Mugika___"
# Reemplazamos solo 3 veces
a = str_content.replace("_", "", 3) # "Hola al curso de Python con Anartz Mugika__"
# Reemplazamos solo 4 veces
a = str_content.replace("_", "", 4) # "Hola al curso de Python con Anartz Mugika_"

print("Final")