d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

list_check_values = [2, 4, 50]
for element in list_check_values:
    # Comprobamos si elemento de búsqueda es clave en diccionario
    if element in d.keys:
        print(f'{element} elemento está presente')
    else:
        print(f'{element} elemento NO está presente')