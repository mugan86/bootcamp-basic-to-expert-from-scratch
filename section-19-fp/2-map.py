# map(funcion, objeto iterable)

# 1

def get_double(element):
    return element * 2

list_int_values = [1, 34, 56, 23, 4, 90]

x = list(map(get_double, list_int_values))
# El resultado esperado
# [2, 68, 112, 46, 8, 180]

x_lambda = list(map(lambda x: x * 2, list_int_values))
print(x)
print(x_lambda)

# 2
def more_than_len_six_characters(word):
    return len(word) > 6

words_list = ["Anartz", "Mugika", "Donostia", "Caracteres"]
x = list(map(more_than_len_six_characters, words_list))

x_lambda = list(map(lambda x: len(x) > 6, words_list))
print(x)
print(x_lambda)