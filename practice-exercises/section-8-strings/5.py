"""
Escribe un programa en C# que donde vamos a introducir dos textos y vamos a comparar si son de la misma longitud y diferentes entre si.
Mostrar lo siguiente después de introducir los dos textos:
Resultado de lo introducido: <primerInput>,< segundoInput>
Longitud de <primerInput> es x carácteres.
Longitud de <segundoInput> es x carácteres.
¿Tienen la misma logitud? <respuesta_true_o_false>
¿Son iguales? (Comparar los dos valores>)

"""

one = input("Introduzca el primer texto:\n")

two = input("Introduzca el segundo texto:\n")

print("Resultado de lo introducido: {}, {}".format(one, two))
print("Longitud de {} es de {} caracteres".format(one, len(one)))
print("Longitud de {} es de {} caracteres".format(two, len(two)))
print("¿Tienen la misma longitud? {}".format(
    len(one) == len(two)
))

print("¿Son iguales? {}".format(
    one == two
))