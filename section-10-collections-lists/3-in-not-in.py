# Vamos a trabajar con el operador de pertenencia en las listas
windows_programs = ["Word", "Excel", "Powerpoint"]

values_check = "Word" in windows_programs # True
values_check = "Word2" in windows_programs # False
values_check = "Excel" in windows_programs # True
values_check = "Word2" not in windows_programs # True

elements = [True, 12 + 24j,  23.3, "anartz"]

values_check = True in elements # True
values_check = False in elements # False
values_check = False not in elements # True
values_check = 12 in elements # False
values_check = 12 + 24j in elements # True
values_check = "anartz" in elements # True
values_check = "anartz3333" in elements # False
values_check = 24.3 not in elements # True
values_check = 23.3 in elements # True

print("********")