# Añadir un elemento

set_one = {'a', True, (45, 45), 'anartz', 34.34}
# {'a', True, (45, 45), 'anartz', 34.34}
set_one.add("Mario Bros")
# {'a', True, (45, 45), 'anartz', 34.34, 'Mario Bros'}
set_one.add("Super Pang")
# # {'a', True, (45, 45), 'anartz', 34.34, 'Mario Bros', 'Super Pang'}

# Añadir un conjunto al conjunto existente
set_two = {True, False, False} # {True, False}
set_one.update(set_two)
# {'a', True, (45, 45), 'anartz', 34.34, 'Mario Bros', 'Super Pang', False}

set_one = { 12, 'a', 'b'}
list_one = [12, -1, 't']
set_one.update(list_one)
# { 12, 'a', 'b', -1 , 't'}
set_one.update("anartz")
# { 12, 'a', 'b', -1 , 't', 'n', 'r', 'z'}

print("FINAL")

