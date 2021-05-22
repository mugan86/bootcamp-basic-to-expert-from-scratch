"""
Convertidor Euros-Pesetas Españolas.
Vamos a crear un programa, donde tenemos un menu inicial con varias opciones que usaremos para seleccionar la que deseamos ejecutar en todo momento.
1 - Convertir una cantidad de euros introducida en pesetas
2 - Convertir una cantidad de pesetas en euros.
3 - Salir.
Si no introducimos correctamente 1,2 mostrar un mensaje “Opción incorrecta. Prueba de nuevo por favor”
Sabiendo que  1 euro = 166,386 pesetas españolas.
Ejemplo:
Euros-> Pesetas = 16 euros son 2.662,176 pesetas españolas
Pesetas->Euros=100000 pesetas españolas son 601,0121euros

"""

print("============CONVERTIDOR============")
print("\t1) Euros a Pesetas")
print("\t2) Pesetas a Euros")
print("===================================")

option = input("Tipo de conversión a realizar: ")
if (option == "1" or option == "2"):
    value = float(input("Cantidad a convertir: "))
    if (option == "1"):	
        print("{0} €uros en Pesetas son: {1}".format(value, value * 166.386))
    elif(option == "2"):
        print("{0} Pesetas en €uros es: {1}".format(value, value / 166.386))
else:
    print("Opción incorrecta")
