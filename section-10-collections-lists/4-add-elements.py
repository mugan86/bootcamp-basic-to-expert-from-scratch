# append()

sagas = ["Sonic", "Mario", "Little Big Planet", "Tomb Raider"]
# ["Sonic", "Mario", "Little Big Planet", "Tomb Raider"]
sagas.append("Assasins Creed")
# ["Sonic", "Mario", "Little Big Planet", "Tomb Raider", "Assasins Creed"]
sagas.append("God of War")
# ["Sonic", "Mario", "Little Big Planet", 
#           "Tomb Raider", "Assasins Creed", "God of War"]
sagas.append("Megaman")
# ["Sonic", "Mario", "Little Big Planet", 
#           "Tomb Raider", "Assasins Creed", "God of War", "Megaman"]


# insert
sagas = ["Sonic", "Mario", "Little Big Planet", "Tomb Raider"]
# ["Sonic", "Mario", "Little Big Planet", "Tomb Raider"]
sagas.insert(0, "Megaman")
# ["Megaman", "Sonic", "Mario", "Little Big Planet", "Tomb Raider"]
sagas.insert(1, "Assasins Creed")
# ["Megaman", "Assasins Creed", "Sonic", "Mario", 
#       "Little Big Planet", "Tomb Raider"]
sagas.insert(0, "God of War")
# ["God of War", "Megaman", "Assasins Creed", "Sonic", "Mario", 
#       "Little Big Planet", "Tomb Raider"]


# extend
list_one = [12, True, "anartz"]
list_two = [23, 23]

list_one.extend(list_two)
# list_one = [12, True, "anartz", 23, 23]

tuple_list = (354, 638393)

list_two.extend(tuple_list)

# list_two = [23, 23, 354, 638393]

print("*******")