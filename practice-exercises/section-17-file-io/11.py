import os

script_directory = os.path.dirname(__file__)

def get_copy_content():
    file_path = f"{script_directory}/exercise11.txt"

    f = open(file_path, "rt")

    return f.read()

def copy_file_content():
    # Crear un nuevo fichero para almacenar la información copiada
    file_path = f"{script_directory}/exercise11-copy.txt"
    f = open(file_path, "w")
    # Escribimos los datos cargados del fichero original
    f.write(get_copy_content())
    # Cerrar flujo
    f.close()

copy_file_content()