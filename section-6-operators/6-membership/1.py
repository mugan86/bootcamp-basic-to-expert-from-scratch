x = ["Python", "Java", "Typescript", "Rust"]

# COmprobar si un valor pertenece a esa variable / objeto

a = "python" in x # False
a = "Python" in x # True

a = "Typescrip" in x # False
a = "Typescript" in x # True

a = "python" not in x # True
a = "Python" not in x # False

a = "Typescrip" not in x # True
a = "Typescript" not in x # False

# cadenas de texto (strings)

x = "Anartz"

a = "a" in x # True
a = "nar" in x # True
a = "anar" in x # False
a = "Anar" in x # True

print("Final")