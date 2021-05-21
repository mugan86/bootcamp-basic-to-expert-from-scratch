'''
Escribe un programa en el que vamos a asignar a un string la siguiente frase “Estoy haciendo los ejercicios opcionales del curso Bootcamp Python 3 con el profesor Anartz Mugika”. 
Vamos a realizar las siguientes comprobaciones y mostramos su resultado. Recordad que son diferentes los mismos carácteres que están en mayúsculas y minúsculas.
(Trabajar con startswith, igualdad ==, endswith)
Comienza con “Bootcamp Python 3”. => false
Comienza con “Estoy haciendo los ejercicios opcionales” => true
Es igual a “Estoy haciendo ejercicios opcionales” => false
Finaliza con “Mugika” => true
Finaliza con “AnartzMugika” => false
Finaliza con “Anartz Mugika” => true"
'''

init_txt = "Estoy haciendo los ejercicios opcionales del curso {}"
all_txt = init_txt.format("Bootcamp Python 3 con el profesor Anartz Mugika")

# Usando 'startswith'
txt = "Comienza con 'Bootcamp Python 3': {}"
check_result = all_txt.startswith('Bootcamp Python 3')
print(txt.format(check_result))
########################
txt = "Comienza con 'Estoy haciendo los ejercicios opcionales': {}"
check_result = all_txt.startswith('Estoy haciendo los ejercicios opcionales')
print(txt.format(check_result))
########################
# Comparando si es igual ==
equal_than = all_txt == "Estoy haciendo ejercicios opcionales"
print("Es igual a 'Estoy haciendo ejercicios opcionales': {}".format(
    equal_than
))
########################
# Usando 'endswith'
txt = "Finaliza con 'Mugika': {}"
check_result = all_txt.endswith("Mugika")
print(txt.format(check_result))
########################
txt = "Finaliza con 'AnartzMugika': {}"
check_result = all_txt.endswith("AnartzMugika")
print(txt.format(check_result))
########################
txt = "Finaliza con 'AnartzMugika': {}"
check_result = all_txt.endswith("Anartz Mugika")
print(txt.format(check_result))


