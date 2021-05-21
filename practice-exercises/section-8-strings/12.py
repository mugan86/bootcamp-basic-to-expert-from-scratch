"""
Escribir un programa en el que vamos a calcular el caracter de control del 
Documento Nacional de Identificación (DNI) de España.
¿Cómo calculamos el caracter de control?
● Tenemos que introducir una entrada de 8 dígitos.
● Tenemos que obtener el resto de la división entre 23 y 
con ese resultado, tenemos
que tener en cuenta la siguiente tabla, para establecer un valor 
u otro seleccionando el elemento correspondiente.
"""
# Introducir el número
dni = int(input("Introduzca número del DNI (8 dígitos): \n"))

# Caracteres de control para asignar al DNI
CHARACTER_CONTROLS = 'TRWAGMYFPDXBNJZSQVHLCKE'

# Mostrar el resultado
print("El DNI completo: {}-{}".format(dni, CHARACTER_CONTROLS[dni % 23]))