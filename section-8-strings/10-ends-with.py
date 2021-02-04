txt = 'Hola, soy Anartz Mugika Ledo y estoy impartiendo este curso de Python'

# Únicamente con la búsqueda de la subcadena

a = txt.endswith('de Python')           # True

a = txt.endswith('curso de Python')     # True

a = txt.endswith('c urso de Python')    # False

a = txt.endswith('curso dePython')      # False

# Especificando los rangos

a = txt.endswith('curso de Python', 10)  # True

a = txt.endswith('Python', 45)            # True

a = txt.endswith('Python', 10, -2)         # False

a = txt.endswith('curso', -15, -10)        # True


print("Final")