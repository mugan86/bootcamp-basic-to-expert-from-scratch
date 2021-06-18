# Inicializar diccionario en blanco

dictionary = dict()

# Bucle para ejecutarse mientras clave sea diferente a EXIT
while True:
    key = input("Introduzca un valor clave. Para salir 'EXIT': ")
    if (key == 'EXIT'):
        # Paramos el bucle
        break
    value = input(f"Introduzca el valor para {key}: " )
    # Actualizar diccionario
    dictionary.update( {
        # Ternario para comprobar si tenemos lista de elementos (list)
        key: (value.split() if (',' in value) else value)
    })
print("EXIT")
print(dictionary)
print(type(dictionary))

        