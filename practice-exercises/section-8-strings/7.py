"""
Escribe un programa que convierta el primer carácter en mayúsculas y 
los restantes 
en minúsculas de un string introducido por teclado.
No usar función 'capitalize'
"""
str_val = input("Introduzca texto a convertir en 'capitalize': \n")
print("==========================================================")
str_capitalize = "{}{}".format(
    str_val[0].upper(),
    str_val[1:].lower()
)
print("{} en 'capitalize' (sin función) => {}".format(
    str_val,
    str_capitalize
))
print('¿Transformado correctamente?: {}'.format(
    str_val.capitalize() == str_capitalize
))
