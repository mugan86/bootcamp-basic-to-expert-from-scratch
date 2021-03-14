# update
set1 = {1, 2, 3, 5, 'a', 'anartz'}
set2 = {True, 12, 12}

set1.update(set2)
# set1 = {1, 2, 3, 5, 'a', 'anartz', 12}
# set2 = {True, 12}

# Obtener un nuevo conjunto a partir de la union => union()
set1 = {1, 2, 3, 5, 'a', 'anartz'}
set2 = {True, 12, 12}

set3 = set1.union(set2)
"""
set1 = {1, 2, 3, 5, 'a', 'anartz'}
set2 = {True, 12, 12}
set3 = {1, 2, 3, 5, 'a', 'anartz', 12}
"""

# Intersección - Solo se añaden los DUPLICADOS
set1 = { 1, 2, 3, 4}
set2 = {1, 4, 5, 2}
set1.intersection_update(set2)
# set1 = { 1, 2, 4}

set1 = { 1, 2, 3, 4}
set3 = set1.intersection(set2)
# set3 = { 1, 2, 4}
# set1 = { 1, 2, 3, 4}
# set2 = {1, 4, 5, 2}

# Obtenemos los valores NO DUPLICADOS
set1 = { 1, 2, 3, 4}
set2 = {1, 4, 5, 2}

set1.symmetric_difference_update(set2)
# set1 = {3, 5}

set1 = { 1, 2, 3, 4}

set3 = set1.symmetric_difference(set2)
# set3 = {3, 5}
# set1 = { 1, 2, 3, 4}
# set2 = {1, 4, 5, 2}
print("FINAL")
