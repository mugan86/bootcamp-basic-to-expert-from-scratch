"""
Crear un programa que determina si una persona te está contestando gritando o no. 
Para especificar que está gritando, tenemos que considerar que el 100% de 
los carácteres del texto que se escribe están en mayúsculas y para ello usamos 
las función “isupper()” (sin argumentos dentro de las cadenas de texto). 
Produrad hacerlo con el operador ternario simple:
Introduce mensaje: hola, soy Anartz!!
Resultado esperado: Mensaje recibido: “NO está gritando”.
==========
Introduce el caracter: HOLA, SOY ANARTZ!!
Resultado esperado: Mensaje recibido: “SI está gritando”.

"""
str_msg = input("Introduce mensaje: \n")

is_anger = "SI está gritando" if (str_msg.isupper()) else "NO está gritando"

print("¿Está enfadado y gritando? {}".format(is_anger))