"""
Hacer un programa haciendo uso del switch que simule un cajero automático
con un saldo inicial de 1000 euros, con el siguiente menú de opciones:
MENÚ:
* Ingresar dinero a la cuenta
* Retirar dinero de la cuenta (si queremos retirar más de lo que hay,
mostrar mensaje advirtiendo que no es posible)
* Salir
(Si no seleccionamos correctamente ni 1,2 ni 3, para decir “Opción incorrecta)

"""

total = 1000

# Comprobar si estamos en el rango correcto del día seleccionado
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta.")
print("3. Salir")

option = input("Selecciona operación: ")

if (option == "1"):
    add_money = float(input("¿Cuánto dinero quieres ingresar? "))
    total += add_money
    print("El saldo de tu cuenta después de añadir {0} euros es de {1} euros.".format(
        add_money, total
    ))
elif (option == "2"):
    quit_money = float(input("¿Cuánto dinero quieres retirar? "))
    if (quit_money > total): print("No puedes retirar {0} euros ya que tu saldo es de {1} euros".format(quit_money, total ))		 
    total -= quit_money
    print("El saldo de tu cuenta después de retirar {0} euros es de {1} euros.".format(
            quit_money, total
    ))
elif(option == "3"):
    print("Saliendo")
else: print("Opción incorrecta. Saliendo")


      
