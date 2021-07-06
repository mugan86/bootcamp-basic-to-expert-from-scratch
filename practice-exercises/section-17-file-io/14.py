import os

file_chars_reference = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_letters_text_files():
    try:
        # Obtenemos la ruta absoluta del directorio en el que estamos trabajando
        script_directory = os.path.dirname(__file__)
        for letter in file_chars_reference:
            file_path = f"{script_directory}/{letter}.txt"
            open(file_path, "w")
    except FileExistsError:
        print("Fichero existe")
        return []
    except Exception as except_message:
        print(except_message)
        return []


create_letters_text_files()
