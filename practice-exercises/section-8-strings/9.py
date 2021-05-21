"""
Escribe un programa en el que vamos a asignar a un string la 
siguiente frase “Estoy haciendo los ejercicios opcionales del curso 
Bootcamp Python 3 con el profesor Anartz Mugika”.
Vamos a realizar las siguientes comprobaciones y mostramos su resultado. 
Recordad que son diferentes los mismos carácteres que están en mayúsculas y 
minúsculas.
(Trabajar con index, selección por rangos)
Extraer “Bootcamp Python 3” teniendo en cuenta que coge el nuevo string 
creado haciendou so de la función index buscando “Bootcamp”. Al obtener 
la posición, tener en cuenta 
la longitud de "Bootcamp Python 3" para extraerlo.
"""
text = "Estoy haciendo los ejercicios opcionales del curso Bootcamp Python 3 con el profesor Anartz Mugika"
# 1 Obtener la posición de la búsqueda "Bootcamp"
find_position = text.index("Bootcamp")

# 2 Aplicamos selección para coger la palabra,
# donde cogemos la posición index y luego especficiamos
# la longitud mediante la propiedad len dentro de "Bootcamp Python 3" y
# sumamos la posición inicial de "find_position"
extract_word = text[find_position:(find_position + len("Bootcamp Python 3"))]

print("Encontrado \"Bootcamp Python 3\" en la posición: {}"
      .format(find_position))
print("Extraido correctamente \"Bootcamp Python 3\": {}"
      .format(extract_word))