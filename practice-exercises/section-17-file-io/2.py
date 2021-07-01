
import os

def print_n_lines(file_name):
    script_directory = os.path.dirname(__file__)
    file_path = f"{script_directory}/{file_name}.txt"
    txt = open(file_path)
    number_of_lines = 3

    for i in range(number_of_lines):
        line = txt.readline()
        print(line)