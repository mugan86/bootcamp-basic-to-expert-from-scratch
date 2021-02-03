# Selecciona subcadena añadiendo pos. inicial / final

variable_one = 'Bienvenido al curso de Python con Anartz Mugika'

a = variable_one[0:10] # 'Bienvenido'
a = variable_one[0:11] # 'Bienvenido '
a = variable_one[0:12] # 'Bienvenido a'
a = variable_one[11:19] # 'al curso'
a = variable_one[11:23] # 'al curso de '
# variable_one = 'Bienvenido al curso de Python con Anartz Mugika'
# Haciendo uso de los índices negativos
a = variable_one[-13:-7] # 'Anartz'
a = variable_one[-17:-7] # 'con Anartz'
a = variable_one[-17:-4] # 'con Anartz Mu'

# Mezclando los índices
a = variable_one[0:-7] # 'Bienvenido al curso de Python con Anartz'
a = variable_one[11:-7] # 'al curso de Python con Anartz'
a = variable_one[23:-4] # 'Python con Anartz Mu'

# Sin especificar la posición inicial (empieza desde 0)
a = variable_one[:10] # 'Bienvenido'
a = variable_one[:11] # 'Bienvenido '
a = variable_one[:12] # 'Bienvenido a'
a = variable_one[:-7] # 'Bienvenido al curso de Python con Anartz'

# Sin especificar la posición final (termina al final del texto)
# Bienvenido al curso de Python con Anartz Mugika
a = variable_one[-13:] # 'Anartz Mugika'
a = variable_one[-6:] # 'Mugika'
a = variable_one[11:] # 'al curso de Python con Anartz Mugika'
a = variable_one[14:] # 'curso de Python con Anartz Mugika'
print("Final")

