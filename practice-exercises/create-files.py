import os

script_directory = os.path.dirname(__file__)
min= 1
max = min + 20
while(min < max +1):
    file_path = f"{script_directory}/section-16-file-io/{min}.py"
    open(file_path, "w")
    min += 1
