"""
Vamos a crear un programa, donde introducimos un número ENTERO entre 0-999 y 
debemos de decir la cantidad de cifras que tiene. Si está fuera de ese rango 
debemos de avisar al usuario que está fuera del rango. 
No lo hagáis usando la clase str, con condicional if
Datos de prueba:
Introduce número: 18
Resultado esperado: El 18 tiene 2 cifras.

"""

number_value = int(input("Introduzca el número a evaluar entre 0-999: "))
if (number_value < 10 and number_value >= 0):
    print(f"El número {number_value} tiene una cifra")
elif (number_value < 100 and number_value >= 10):
    print(f"El número {number_value} tiene dos cifras")
elif (number_value < 1000 and number_value >= 100):
    print(f"El número {number_value} tiene tres cifras")
else:
    print(f"El número {number_value} está fuera del rango 0-999")