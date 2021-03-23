try:
    # Código del programa
    print("jjjj")
    list_values = ['anartz', 'mugika', 'ledo']
    number_one = float(input('Introduzca valor 1: '))
    number_two = float(input('Introduzca valor 2: '))
    division = number_one / number_two
    print(list_values[1])
    # Destruimos la lista para que no exista y de excepción NameError
    del list_values
    print(list_values[1])
except KeyboardInterrupt:
    print("Hemos parado el programa con CTRL + C")
except NameError:
    print("El valor seleccionado no existe actualmente")
except IndexError:
    print("El indice seleccionado no es accesible por no existir")
except ZeroDivisionError:
    print("Error por dividir por cero")
except ValueError:
    print("No podemos introducir un string en un valor numérico")
except Exception as except_message:
    print(except_message)

print("Final")