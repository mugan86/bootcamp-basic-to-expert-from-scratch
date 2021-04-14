# filter(funcion para filtrar la info, objeto iterable)

# 1

def check_is_int(element): return type(element) == int

set = {'Anartz', 10, 1, 2, 3, 4, 567, 23 + 45j, 34.5}
x = list(filter(check_is_int, set))
# [10, 1, 2, 3, 4, 567]
print(x)

x_lambda = list(filter(lambda x: type(x) == int, set))
print(x_lambda)
# [10, 1, 2, 3, 4, 567]

# 2 Mostrar únicamente los valores con longitud par

def get_only_par_len(word): return len(word) % 2 == 0

names = ("Anartz", "Ana", "Mikel", "Donostia", "Bilbao_", "Tomb Raider")

x = list(filter(get_only_par_len, names))
# ["Anartz", "Donostia"]
print(x)

x_lambda = list(filter(lambda x: len(x) % 2 == 0, names))
# ["Anartz", "Donostia"]
print(x_lambda)

# Ahora hacemos con los valores impares

def get_only_impar_len(word): return len(word) % 2 != 0

names = ("Anartz", "Ana", "Mikel", "Donostia", "Bilbao_", "Tomb Raider")

x = list(filter(get_only_impar_len, names))
# ["Ana", "Mikel", "Bilbao_", "Tomb Raider"]
print(x)

x_lambda = list(filter(lambda x: len(x) % 2 != 0, names))
# ["Ana", "Mikel", "Bilbao_", "Tomb Raider"]
print(x_lambda)