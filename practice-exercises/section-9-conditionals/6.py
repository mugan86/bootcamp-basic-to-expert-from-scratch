"""
Escribe un programa en en el que introducimos un número de 1 a 12 (incluidos) 
para hacer referencia al mes seleccionado. Una vez introducidos tenemos que 
devolver el número de días que tiene ese mes.
 Hay que tener en cuenta si el mes seleccionado es 2 (Febrero), deberíamos de 
 pedir el año para ver si ese año es bisiesto o no y con ello dar 29 días 
 (Bisiesto) o 28 días (No Bisiesto)

Meses con 31 días:
Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre
Meses con 30 días:
Abril, Junio, Septiembre, Noviembre
Febrero:
28 días si NO BISIESTO
29 días si BISIESTO
"""

month = int(input("Introduzca el mes (1 y 12): \n"))

if (month >= 1 and month <= 12):  # mes válido
    if(month == 2):  # febrero => ¿Bisiesto?
        year = int(input("Introduzca el año: \n"))
        if ((year % 100 != 0 and year % 4 == 0) or year % 400 == 0):
            print("Este mes al ser febrero y BISIESTO tiene 29 días")
        else:
            print("Este mes al ser febrero y NO BISIESTO tiene 28 días")
    elif(month == 1 or month == 3 or month == 5 or month == 7
         or month == 8 or month == 10 or month == 12):
        print("Este mes tiene 31 días")
    else:
        print("Este mes tiene 30 días")
else:
    print("Debes de introducir un número entre 1 y 12 (incluido)")
