"""
Escribir un programa que obtiene el contenido de un fichero de texto 
y devuelve el número de palabras que contiene.
Tener en cuenta: Algunas palabras están separadas por punto y coma, 
eliminarlos antes de hacer el cómputo.
"""

import os
file_name = "exercise1"
def get_filelines_content():
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        file_path = f"{script_directory}/{file_name}.txt"
        return clean_scape_characters(open(file_path).readlines())
    except FileNotFoundError:
        print("No podemos abrir el fichero por no existir")
        return []
    except Exception as except_message:
        print(except_message)
        return []

# Limpiamos el contenido de caracteres de escape y devolverlo limpio
def clean_scape_characters(list):
    clean_list = []
    for i in range(len(list)):
        list[i] = list[i].replace('.','').replace(',', '')
        elements = list[i].split()
        clean_list.extend(elements)
    return clean_list
word_list = get_filelines_content()
word_list_length = len(word_list)
print(f"El fichero tiene {word_list_length} palabras")