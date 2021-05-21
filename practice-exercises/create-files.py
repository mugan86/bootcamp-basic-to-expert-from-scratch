import os

script_directory = os.path.dirname(__file__)
min= 12
max = min + 4
while(min < max +1):
    file_path = f"{script_directory}/section-8-strings/{min}.py"
    open(file_path, "w")
    min += 1
