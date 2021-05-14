import os

script_directory = os.path.dirname(__file__)
min= 18
max = 45
while(min < max +1):
    file_path = f"{script_directory}/{min}.py"
    open(file_path, "w")
    min += 1
