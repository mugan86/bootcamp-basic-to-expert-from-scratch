"""


"""

import os
file_name = "exercise10"
result_fle_name = "exercise10-result"
result = []
# Obtenemos la ruta absoluta del directorio en el que estamos trabajando
script_directory = os.path.dirname(__file__)
def get_file_content():
    try:
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

def get_word_appears_count():
    word_list = get_file_content()
    # Usamos la lista de todas las palabras del fichero
    for word in word_list:
        # Si no hay nada en el resultado, almacenar palabra con 1 aparición
        if (len(result) == 0):
            result.append([word, 1])
        else:
            # Recorrer el resultado para ver si hay apariciones
            for position in range(len(result)):
                # Si encuentra algo, sumar + 1 la aparición
                if (word in result[position]): 
                    result[position][1] += 1
                    break
                # Si recorre todo los resultados y no encuentra nada, nuevo elemento
                elif position == len(result) - 1:
                    result.append([word, 1])
def save_result():
    file_path = f"{script_directory}/{result_fle_name}.txt"
    # "w" para sobrescribir lo anterior
    txt = open(file_path, "w")
    for element  in result:
        txt.write(f"{element[0]}, {element[1]}\n")
    txt.close()

# Obtener las apariciones
get_word_appears_count()
# Guardar resultado
save_result()