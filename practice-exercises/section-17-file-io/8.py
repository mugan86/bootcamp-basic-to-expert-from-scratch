"""
 Utilizando como base el ejercicio anterior, vamos a implementar 
 la función para que almacene una ó más palabras en una lista, 
 en el caso de que haya más de una palabra con la longitud máxima 
 que sea igual.
El resultado que obtendremos será el siguiente:
Si hay un resultado:
La palabra de más longitud es <palabra> y su longitud es de <longitud>
 caracteres.
Si hay dos ó más resultados:  
Las palabras de más longitud son <lista-palabras> y su longitud es de 
<longitud> 

"""

import os
file_name = "exercise8"
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

def get_longest_words(word_list):
    max_longitude_words_count = get_longest_count(word_list)
    max_longitude_words_list = []
    for element in word_list:
        if(max_longitude_words_count == len(element)): 
            max_longitude_words_list.append(element)
    return (
        max_longitude_words_count,
        max_longitude_words_list
    )

def get_longest_count(word_list):
    print(word_list)
    longest_count = len(word_list[0])
    for i in range(1, len(word_list)):
        if (longest_count < len(word_list[i])):
            longest_count = len(word_list[i])
    return longest_count

word_list = get_filelines_content()

list_max_characters_words = get_longest_words(word_list)

if (len(list_max_characters_words[1]) == 1):
    print(f"La palabra '{list_max_characters_words[1][0]}' tiene la " + \
            f"longitud máxima con {list_max_characters_words[0]} caracteres")
else:
    print(f"Las palabras '{list_max_characters_words[1]}' tienen la " + \
            f"longitud máxima con {list_max_characters_words[0]} caracteres")