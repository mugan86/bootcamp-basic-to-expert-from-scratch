"""


"""

import os
file_name = "exercise7"
def get_filelines_count():
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        return len(open(file_path).readlines())
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
        return 0
    except Exception as except_message:
        print(except_message)
        return 0

# Iprimir las líneas que contiene el fichero
print(get_filelines_count())