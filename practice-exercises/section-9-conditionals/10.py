"""
Una tienda de videojuegos desea un programa para ingresar el valor de compra y 
calcular lo siguiente: si el pago se efectúa al “contado”, calcular un descuento 
del 10% pero si el pago es con “tarjeta” se incrementa un recargo del 2% al 
valor de compra. Calcular y visualizar el descuento o recargo según sea el caso 
y el total a pagar de la compra.
"""

total = float(input("Introduce el importe a pagar: "))

pay_mode = input("¿Cómo vas a pagar? Tarjeta (T) / Contado (C)? ")
print("===================================")
print("Valor del producto: {0}".format(total))
extra_pay = 0
if (pay_mode == "C" or pay_mode == "c"):
	extra_pay = -(total * 10 / 100)
	print(f"Descuento (10%) - Pago al contado: {extra_pay:.2f}")
elif (pay_mode == "T" or pay_mode == "t"): 
	extra_pay = (total * 2 / 100)
	print(f"Recargo (2%) - Pago con tarjeta: {extra_pay:.2f}")
print(f"Total a pagar: {(total + extra_pay):.2f}")