"""
Vamos a crear un programa, donde introducimos un año cualquiera (número ENTERO)
y comprobamos si es bisiesto o no el año.
Tenemos que tener en cuenta lo siguiente, para saber si es un año bisiesto o no:

Hay que tener estas condiciones, con que cumpla una de ellas es suficiente:
No divisible de 100 y divisible de 4. Si cumple Bisiesto. Si no, No bisiesto
Divisible de 400. Si cumple => Bisiesto. Si no cumple seguir al siguiente paso.
Datos de prueba:
Introduce un año: 2016
Resultado esperado: 2016 es BISIESTO.
Introduce el número: 2017
Resultado esperado: 2017 NO es BISIESTO.
Pista, mediante operadores lógicos podemos hacer la pregunta para saber si es
bisiesto o no, tener en en cuenta el uso de paréntesis, AND, OR,...
Los años bisiestos entre 1582 y 2200: 
https://miniwebtool.com/es/leap-years-list/?end_year=2200&start_year=1582

"""

number_val = int(input("Introduzca el año a comprar si es bisiesto o no: \n"))

"""(No divisible de 100 y divisible de 4 
o  Divisible de 400)Si cumple => Bisiesto. 

ELSE => Si no cumple seguir al siguiente paso.
"""

if ((number_val % 100 != 0 and number_val % 4 == 0) or number_val % 400 == 0): 
    result = " es BISIESTO"
else:
    result = " NO es BISIESTO"

print(f"{number_val}{result}")
