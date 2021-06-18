import os

script_directory = os.path.dirname(__file__)
min= 1
max = min + 10
while(min < max +1):
    file_path = f"{script_directory}/section-14-dicts/{min}.py"
    open(file_path, "w")
    min += 1
