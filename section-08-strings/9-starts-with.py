txt = 'Hola, soy Anartz Mugika Ledo y estoy impartiendo este curso de Python'

# Únicamente con la búsqueda de la subcadena

a = txt.startswith('Hola, soy')         # True

a = txt.startswith('Hola, soy Anartz')  # True

a = txt.startswith('Hola, soy Anart z') # False

a = txt.startswith('Hola,soy')          # False

# Especificando los rangos

a = txt.startswith('Hola, soy Anartz', 10)  # False

a = txt.startswith('Anartz', 10)            # True

a = txt.startswith('Anartz', 9, -2)         # False

a = txt.startswith(' Anartz', 9, 20)        # True


print("Final")