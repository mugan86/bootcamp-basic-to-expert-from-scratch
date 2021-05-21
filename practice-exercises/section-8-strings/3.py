"""
Escribe un programa que concatene en una variable con la función format 
los tres textos que vamos a introducir desde el teclado en la consola, 
tiene que estar separados por un tabulador entre palabras y finalmente 
imprimimos el resultado de la variable nueva. 
Procurad tener en cuenta el salto de línea para el texto que se introduce.
"""
one = input("Introduzca el primer texto:\n")

two = input("Introduzca el segundo texto:\n")

three = input("Introduzca el tercer texto:\n")

result_one = "Resultado de los tres textos concatenados y añadidos "
result_second = " con tabulación: {}\t{}\t{}"
print((result_one + result_second).format(one, two, three))