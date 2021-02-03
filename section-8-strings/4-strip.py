# Eliminar inicio / final de los caracteres seleccionados

# Valores por defecto - Espacios en blanco
a = "   Anartz  Mugika     ".strip() # 'Anartz  Mugika'
a = "        Anartz    Mugika ".strip() # 'Anartz    Mugika'

# Valores personalizados
a = "... Anartz  Mugika     ".strip('.') # ' Anartz  Mugika     '
a = "... Anartz  Mugika     ".strip('. ') # 'Anartz  Mugika'
a = "...!! Anartz @@!!!Mugika  ???@   ".strip('. ?@!') # 'Anartz @@!!!Mugika'

print("Final")