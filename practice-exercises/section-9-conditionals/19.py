"""
Una distribuidora de motocicletas tiene una promoción de fin de año que 
consiste en lo siguiente. Las motos marca Honda tienen un descuento del 5%, 
las marcas Yamaha del 8% y las Suzuki del 10%, las otras marcas 2%. 
Hay que pedir el nombre de la marca (se puede hacer con un menú inicial 
con las opciones para seleccionar) de la moto y también el precio de la moto.
"""

print("============MOTOS============")
print("1) Honda")
print("2) Yamaha")
print("3) Suzuki")
print("4) Otra marca")
print("========================")

option = input("Seleccione la marca:\n")
if (option == "1" or option == "2" or option == "3" or option == "4"):
    price = float(input("Precio a pagar:\n"))
    if (option == "1"):
        print(f"Honda (Descuento %5) = {price - (price * 0.05)}" )
    elif (option == "2"): 
        print(f"Yamaha (Descuento %8) = {price - (price * 0.08)}" )
    elif (option == "3"): 
        print(f"Suzuki (Descuento %10) = {price - (price * 0.1)}" )
    elif (option == "4"): 
        print(f"Otras (Descuento %2) = {price - (price * 0.02)}" )
else:
    print("Opción incorrecta")