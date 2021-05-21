# Introducir el número
dni = int(input("Introduzca número del DNI (8 dígitos): \n"))

# Caracteres de control para asignar al DNI
CHARACTER_CONTROLS = 'TRWAGMYFPDXBNJZSQVHLCKE'

# Mostrar el resultado
print("El DNI completo: {}-{}".format(dni, CHARACTER_CONTROLS[dni % 23]))