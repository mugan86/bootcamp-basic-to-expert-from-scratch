# Bucle while por defecto
total = 0
counter = 1

# counter = 1 / total = 0
while counter <= 3 or total <= 14:
    total += counter        # 1, 3, 6, 10, 15
    counter += 1            # 2, 3, 4, 5, 6


# Bucle while con "break"

total = 0
counter = 1

# counter = 1 / total = 0
while counter <= 3 or total <= 14:
    total += counter        # 1, 3
    if (counter == 2):
        break
    counter += 1            # 2

# Bucle while con "continue"

total = 0
counter = 1

# counter = 1 / total = 0
while counter <= 3 and total <= 14:
    total += counter        # 1, 3, 5, 7, 9, 11, 13, 15
    if (counter == 2):
        continue
    counter += 1            # 2

# Bucle while con "else"

total = 0
counter = 1

# counter = 1 / total = 0
while counter <= 3:
    total += counter        # 1, 3, 6
    counter += 1            # 2, 3, 4
else: 
    total = "Else ejecutando - else"
# Bucle while con "else" con "break"

total = 0
counter = 1
while counter <= 3:
    total += counter        # 1, 3
    if (counter == 2 ):
        break
    counter += 1            # 2
else: 
    total = "(break) Else ejecutando - usando break"

print("FINAL")