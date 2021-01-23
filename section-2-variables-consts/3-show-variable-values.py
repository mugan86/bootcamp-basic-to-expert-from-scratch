int_val, str_val_one, str_val_two, float_number = 1, "333", "AA", 2.22

# Variable con texto 

print("Primer texto: " + str_val_one)

# combinación de dos variables de tipo texto
print(str_val_one + str_val_two) # 333AA

# combinación de dos variables de tipo numérico
print(int_val + float_number) # 3.22

# combinación de dos variables de tipo numérico y tipo string (ERROR!!)
print(str_val_one + str(float_number)) # "3332.22"
print("Último texto: " + str(int_val)) # "Último texto: 1"