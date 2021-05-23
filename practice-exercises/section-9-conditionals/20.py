"""
Un obrero necesita calcular su salario semanal, el cual se obtiene de la 
siguiente manera:
Si trabaja 40 horas o menos se le paga 16 euros por hora
Si trabaja mas de 40 horas se le paga 16 euros por cada una de 
las primeras 40 horas y 20 euros por cada hora extra.
"""

print("============SALARIO SEMANAL OBRERO============")
hours_work = int(input("Horas trabajadas: "))
if (hours_work <= 40):
	print("El salario semanal del trabajador por trabajar {0} horas es: {1}".format(
        hours_work, hours_work * 16
    ))
else :
    extraHours = hours_work - 40
    print(f"El trabajador ha trabajado 40 horas con {extraHours} horas extras")
    print(f"El salario semanal por 40 horas son {40 * 16}")
    print(f"El salario semanal por {extraHours} horas extras son {extraHours * 20}")
    print("El salario semanal del trabajador por trabajar {0} es {1}".format(
        hours_work, (40*16) + (extraHours * 20)
    ))
