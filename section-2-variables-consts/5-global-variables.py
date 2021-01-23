# Variables globales sin hacer uso de palabra "global"

"""
CLASE 1 - Variables globales sin "global"
PRIMER CASO CON SOLO VARIABLE GLOBAL
variable_global = "Hola Mundo"

def custom_function():
    print(variable_global)

print("Fuera: " + variable_global)
# Llamar a la función para ejecutarla
custom_function()


variable_global = "Hola Mundo"

def custom_function():
    variable_global = "Hola Mikel"
    print(variable_global)
    variable_global = "Hola Anartz"
    print(variable_global)

print("Fuera: " + variable_global)
# Llamar a la función para ejecutarla
custom_function()
"""

# Haciendo uso de la palabra clave "global"
name = "Anartz"
def use_global_function_value():
    global name
    name = "Mikel Mikel Mikel"


use_global_function_value()
print("Name: " + name)