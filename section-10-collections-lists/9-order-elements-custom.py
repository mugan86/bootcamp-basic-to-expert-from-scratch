# Establecemos el criterio de ordenación

def order_by_last_char(n):
    return n[len(n) - 1]

str_list = ["javascript", "scala", "cobol", "c#", "python"]

str_list.sort(key=order_by_last_char)
# t, a, l, #, n
#     #, a, l, n, t => c#, scala, cobol, python, javascript

str_list.sort(key=order_by_last_char, reverse=True)
# t, a, l, #, n
#     t, n, l, a, # => , javascript, python, cobol, scala, c#

print("*********")
