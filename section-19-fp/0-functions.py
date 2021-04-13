# Funciones para el saludo

def hello(name = "amig@s"):
    return f"¡Hola {name}!"

def goodbye(name = "amig@s"):
    return f"¡Adios {name}!"

def message(function, name):
    return function(name)

names = ["Anartz", "Ruslan", "Mikel"]
function_hello = hello

for name in names:
    result = message(function_hello, name)
    print(result)

function_goodbye = goodbye

for name in names:
    result = message(function_goodbye, name)
    print(result)