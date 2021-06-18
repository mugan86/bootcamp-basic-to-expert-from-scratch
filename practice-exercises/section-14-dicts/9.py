califications = {
    'anartz': 9.99,
    'mikel': 5.01,
    'aitor': 1.22,
    'maite': 10,
    'miren': 7.8,
    'olatz': 9.89
}
pass_students = []

# Obtener clave, valor elemento a elemento
for key, value in califications.items():
    if (value >= 5): pass_students.append(key)

print("Notas del curso:")
print(califications)
print("Aprobados:")
print(pass_students)
