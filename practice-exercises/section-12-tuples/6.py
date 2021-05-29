"""
Crear una tupla desde el siguiente texto: “Bootcamp Python 3 - Curso desde 0”.
Debemos de realizar:
Obtener el tercer elemento desde el inicio y desde el final de una tupla especificada. 
Rangos que se especifican a continuación:
Desde el inicio (posición 0) a la 5 incluida)
Desde la 5 hasta el final (incluida)
Desde la 5ª posición empezando desde el final hasta el final (incluido)


"""

tuple_chars = tuple("Bootcamp Python 3")
print(tuple_chars)
print("Desde el 3er elemento hasta no coger los últimos 3 elementos")
print(tuple_chars[2:-3])
print("Desde el 5ª elemento hasta el final")
print(tuple_chars[5:])
print("Desde el 5ª elemento hasta los últimos 5 elementos")
print(tuple_chars[5:-5])