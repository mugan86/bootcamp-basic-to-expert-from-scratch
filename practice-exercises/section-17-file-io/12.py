import os

script_directory = os.path.dirname(__file__)
path = f"{script_directory}/exercise11.txt"
f = open(path,'r')
# Preguntamos si hemos cerrado el flujo del fichero
print(f.closed) # False
f.close()
print(f.closed) # True