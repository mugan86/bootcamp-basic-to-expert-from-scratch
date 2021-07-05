"""


"""

import os
file_name = "exercise10"
def get_file_content():
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        return clean_scape_characters(open(file_path).readlines())
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
        return 0
    except Exception as except_message:
        print(except_message)
        return 0

# Limpiamos el contenido de caracteres de escape y devolverlo limpio
def clean_scape_characters(list):
    clean_list = []
    for i in range(len(list)):
        list[i] = list[i].strip()
        elements = list[i].split()
        clean_list.extend(elements)
    return clean_list