"""
Lo mismo que en el anterior, pero limpiando los caracteres de escape
"""

import os
file_name = "exercise4"
def get_filelines_content():
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        return open(file_path).readlines()
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
        return []
    except Exception as except_message:
        print(except_message)
        return []

# Limpiamos el contenido de caracteres de escape y devolverlo limpio
def clean_scape_characters(list):
    for i in range(len(list)):
        list[i] = list[i].strip()
    return list

print(clean_scape_characters(get_filelines_content()))