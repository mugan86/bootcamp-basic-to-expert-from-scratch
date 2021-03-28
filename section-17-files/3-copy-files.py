import os

script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/1.txt"

f = open(file_path, "rt")

copy_data = f.read()

# Crear un nuevo fichero para almacenar la información copiada
file_path = f"{script_directory}/1-copy.txt"
f = open(file_path, "w")
f.write(copy_data)

f.close()
print("Final")