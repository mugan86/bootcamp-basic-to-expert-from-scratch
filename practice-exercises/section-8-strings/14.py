"""
Siguiendo el ejercicio anterior, vamos a añadirle un apartado donde 
nos muestra un mensaje “Seleccione la opción deseada” 
(sin NINGÚN SALTO DE LÍNEA) y leer mediante teclado lo que introducimos.
Preguntamos mediante el operador relacional: ¿Está entre 1 y 4 (incluidos)?
¿Es igual a 5?
"""
print("===========================================================")
print("\t\tAHORCADO - OPCIONES DEL JUEGO")
print("===========================================================")
print("1) Jugar a acertar una palabra aleatoria.")
print("2) Jugar a acertar cinco palabras aleatorias.")
print("3) Jugar a acertar una palabra de un tema seleccionado")
print("4) Jugar a acertar cincos palabras de un tema seleccionado")
print("5) Salir.")
print("===========================================================")

select_option = int(input("Seleccione la opción deseada: "))

check_one = select_option >= 1 and select_option <= 4
print("¿Está entre 1 y 4 (incluidos)? {}".format(check_one))
check_two = select_option == 5
print("¿Hemos seleccionado salir? {}".format(check_two))