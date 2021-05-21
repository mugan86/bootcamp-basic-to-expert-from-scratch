"""
Escribe un programa que concatene en dos variables, por un lado con la 
función “format” y por otro con “f-string” una lista de 5 productos 
que se mostrarán solo CON UN print y su contenido, elemento a elemento 
tendrán un salto de línea (mirar bien los carácteres de escape).
"""
one = input("Introduzca el primer producto:\n")

two = input("Introduzca el segundo producto:\n")

three = input("Introduzca el tercer producto:\n")

four = input("Introduzca el cuarto producto:\n")

five = input("Introduzca el quinto producto:\n")

result_one = "Resultado de los tres textos concatenados usando "
result_second = " format:\n{}\n{}\n{}\n{}\n{}"
print((result_one + result_second).format(one, two, three, four, five))
print("==========================================================")
result_second = f" f-string:\n{one}\n{two}\n{three}\n{four}\n{five}"
print(result_one + result_second)