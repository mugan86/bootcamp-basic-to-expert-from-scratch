"""
Leer de un fichero todas las líneas y extraer la información sin 
caracteres de escape (por ejemplo salto de línea) y determinar cual 
de ellos es la palabra más larga. Procurad que solo haya una palabra 
más larga respecto a las otras.
En el resultado determinar la palabra más larga y cuantos caracteres 
de longitud tiene.

"""

import os
file_name = "exercise7"
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
        list[i] = list[i].strip()
        elements = list[i].split()
        clean_list.extend(elements)
    return clean_list

def get_longest_word(word_list):
    longest_count = len(word_list[0])
    longest_word = word_list[0]
    for i in range(1, len(word_list)):
        if (longest_count < len(word_list[i])):
            longest_count = len(word_list[i])
            longest_word = word_list[i]
    return f"La palabra '{longest_word}' es la de + " + \
        f"longitud con {longest_count} caracteres"

word_list = get_filelines_content()


print(get_longest_word(word_list))
