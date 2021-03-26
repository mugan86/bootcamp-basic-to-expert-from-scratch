# Abrir el fichero especificando nuestra ruta de la carpeta

import os

script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/1.txt"

f = open(file_path)

print(f.read())

# Vamos a leer 13 caracteres
f = open(file_path)
print("Obtenemos 13 caracteres")
print(f.read(13))

# Vamos a leer línea a línea con el cursor
f = open(file_path)
print("Línea 1")
print(f.readline())
print("Línea 2")
print(f.readline())
print("Línea 3")
print(f.readline())

# Recorremos con el "for"
print("Añadimos todos con un \"for\"")
f = open(file_path)
for line in f:
    print(line)
f.close()

print("final")