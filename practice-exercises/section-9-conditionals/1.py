"""
Vamos a crear un programa, que acepta dos números ENTEROS y comprobamos si son iguales o no.
Datos de prueba:
Introduce el primer número: 5
Introduce el segundo número: 6.
Resultado esperado: ¿Son iguales 5 y 6? NO.

Introduce el primer número: 5
Introduce el segundo número: 5.
Resultado esperado: ¿Son iguales 5 y 5? SI.

"""

one_number = int(input("Introduce el primer número: \n"))

two_number = int(input("Introduce el segundo número: \n"))


if (one_number == two_number): result_equal = True
else: result_equal = False

print(f"¿Son iguales {one_number} y {two_number}?: {result_equal}")