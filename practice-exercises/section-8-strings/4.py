"""
Escribe un programa que concatene en una variable con la función “format” 
los tres textos que vamos a introducir desde el teclado en la consola, 
dichas palabras tienen que estar con un salto de línea (\n) 
y finalmente imprimimos el resultado de la variable nueva.
"""
one = input("Introduzca el primer texto:\n")

two = input("Introduzca el segundo texto:\n")

three = input("Introduzca el tercer texto:\n")

result_one = "Resultado de los tres textos concatenados y añadidos "
result_second = " con salto de línea:\n{}\n{}\n{}"
print((result_one + result_second).format(one, two, three))