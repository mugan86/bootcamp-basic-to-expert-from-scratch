"""
“,”, “.”, “@”, “-” 
"""

str_value = "Estoy en la parte de la clase String del curso de ‘Bootcamp Python 3’ con el profesor" + \
    " Anartz Mugika. Luego aprenderé a trabajar con las estructuras de control del flujo de un programa :)" + \
        "Voy a escribir un correo electrónico a anartzmugika@anartz.com para preguntar una duda"

str_value = str_value.replace('.', '_').replace('@', '_').replace(',', '_').replace('-', '_')
str_phrases = str_value.split('_')

print("Nº Frases obtenidas: {}".format(len(str_phrases)))
print("Frase 1: {}".format(str_phrases[0]))
print("Frase 2: {}".format(str_phrases[1]))
print("Frase 3: {}".format(str_phrases[2]))
print("Frase 4: {}".format(str_phrases[3]))