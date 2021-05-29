"""
Creamos una tupla con un carácter por posición y mediante un bucle, creamos un string final.
Ejemplo:
tupla inicial = (‘a’, ‘n’, ‘a’, ‘r’, ‘t’, ‘z’)
string final = “anartz”
"""

tuple_chars = ('a', 'n', 'a', 'r', 't', 'z')

result = ''
for char_item in tuple_chars:
    result += char_item

print(result)