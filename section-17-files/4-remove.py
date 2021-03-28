import os

script_directory = os.path.dirname(__file__)
file_path = f"{script_directory}/2.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("{} eliminado correctamente".format(file_path))
else:
    print("{} NO existe y no se puede eliminar".format(file_path))