import os

script_directory = os.path.dirname(__file__)
min= 1
max = min + 19
while(min < max +1):
    file_path = f"{script_directory}/section-9-conditionals/{min}.py"
    open(file_path, "w")
    min += 1
