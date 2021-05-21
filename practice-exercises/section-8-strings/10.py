"""
Escribe un programa en el que vamos a asignar a un string la siguiente 
frase “Estoy en la parte de la clase String del curso de ‘Bootcamp Python 3’
con el profesor Anartz Mugika. Luego aprenderé a trabajar con las 
estructuras de control del flujo de un programa :)”. 

Vamos a extraer con split separando con el carácter “.” y asignaremos dentro de un list y evaluamos su longitud que debe de ser 2 (la longitud se evalua como un str). Acceder a las posiciones index 0 y 1 también.
(Trabajar con split)

"""

str_value = "Estoy en la parte de la clase String del curso de ‘Bootcamp Python 3’ con el profesor" + \
    " Anartz Mugika. Luego aprenderé a trabajar con las estructuras de control del flujo de un programa :)"

str_phrases = str_value.split('.')
print("Nº Frases: {}".format(len(str_phrases)))
print("Frase 1: {}".format(str_phrases[0]))
print("Frase 2: {}".format(str_phrases[1]))
