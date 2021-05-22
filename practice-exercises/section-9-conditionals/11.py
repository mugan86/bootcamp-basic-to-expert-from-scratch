"""
La academia de Formación “Anartz Mugika Ledo Online” desea un programa para
ingresar por teclado el total de compra y el día de la semana si el día es
martes o jueves, se realizará un descuento del 15% por la compra. Si el día es
domingo, se descontará un 29% del total de la compra.
Visualizar el descuento y el total a pagar por la compra. Hay que tener en
cuenta que tienes que añadir un menú asociado para introducir un número entre
1-7 (incluidos) para hacer referencia a los días de la semana.
Hay que hacer una comprobación que introducimos un día de la semana correcta.
Si no está dentro del rango, NO SE APLICA DESCUENTO mostrando un mensaje
"El día de la semana es inexistente y no hay descuento para aplicar.

"""

total = float(input("Introduce el importe total a pagar: "))
print("¿Qué día de la semana es?")
print("1) Lunes")
print("2) Martes")
print("3) Miércoles")
print("4) Jueves")
print("5) Viernes")
print("6) Sábado")
print("7) Domingo")
week_day = int(input("Introduce día de la semana: "))
print("=============================================")
print("Día introducido: {0}".format(week_day))
discount_value = 0
# Comprobar si estamos en el rango correcto del día seleccionado
if (week_day >= 1 and week_day <= 7):
    # Comprobar si es martes o jueves
    if (week_day == 2 or week_day == 4):  # 15% de descuento
        discount_value = total * 0.15
        print(f"Total a pagar (15% descuento) = {(total-discount_value):.3f}")
    elif(week_day == 7):
        discount_value = total * 0.29
        print(f"Total a pagar (29% descuento) = {(total-discount_value):.3f}")
    else:
        print(f"Total a pagar (sin descuento) = {total:.3f}", )
else:
    print("El día de la semana es inexistente y no hay descuento para aplicar")
    print(f"Total a pagar (sin descuento) = {total:.3f}")
