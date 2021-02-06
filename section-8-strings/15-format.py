"""
Trabajaremos con format()
<string> = 'Texto {}'
<string>.format(...argumentos)
"""

# 1.- Sin posición index asignada
name = "Tomb Raider 2"
# 1.1.- Con un valor
a = 'Mi juego favorito es {}'.format(name)
# Mi juego favorito es Tomb Raider 2

# 1.2.- + de un valor
name_first_game = "Tomb Raider 2"
name_second_game = "Little Big Planet"
a = 'Mis juegos favoritos son {} y {}.'.format(
    name_first_game, name_second_game)
# Mis juegos favoritos son Tomb Raider 2 y Little Big Planet

# 2.- Asignando posición index para especificar como ordenarlo
a = 'Mis juegos favoritos son {1} y {0}.'.format(
    name_first_game, name_second_game)
# Mis juegos favoritos son Little Big Planet y Tomb Raider 2 

name_third_game = "GTAV"
a = 'Mis juegos favoritos son {2}, {0} y {1}.'.format(
    name_first_game, name_second_game, name_third_game)
# Mis juegos favoritos son GTAV, Little Big Planet y Tomb Raider 2 
print("Final")