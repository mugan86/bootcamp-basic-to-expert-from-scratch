# cadena de texto que vamos a convertir en diccionario con clave numérica
# y el valor de la letra
contro_letters_str = 'TRWAGMYFPDXBNJZSQVHLCKE'

# diccionario donde se almacenará clave numérica y valor de la letra
dict_control_letters = {}
for position in range(len(contro_letters_str)):
    dict_control_letters.update({position: contro_letters_str[position]})

print(dict_control_letters)

dni_number = input("Introduzca el número del DNI: ")
if (len(dni_number) == 8):
    print(f'{dni_number} - {dict_control_letters.get(int(dni_number) % 23)}')
else:
    print("El número DEBE de tener 8 dígitos")
