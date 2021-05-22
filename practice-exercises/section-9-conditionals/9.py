"""
Vamos a crear un programa que simule un inicio de sesión solicitando el nombre de usuario y contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto / nombre de usuario y/o contraseña incorrecto. (por ejemplo el usuario vuestro nombre en minúsculas (bootcamp_python3) y el password 12345678
Datos de prueba:
Introduce usuario: bootcamp_python3 / Introduce el password: 12345678
Resultado esperado: Sesión iniciada correctamente.
=================================================
Introduce usuario: bootcamp_python3 / Introduce el password: 1234
Resultado esperado: nombre de usuario y/o contraseña incorrecto.

"""
user = input("Introduce el usuario: ")
password = input("Introduce la contraseña: ")
print("===================================")

if (user == "bootcamp_python3" and password == "12345678"):
    print("Credenciales correctos. Se ha iniciado sesión \"bootcamp_python3\"")
else:
    print("Los datos de sesión no son correctos. Prueba de nuevo por favor.")
