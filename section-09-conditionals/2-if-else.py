print("Notas obtenidas en los exámenes")
graphql = float(input("GraphQL: "))
npm = float(input("NPM: "))
c_sharp = float(input("C#: "))
meang = float(input("MEAN+G: "))

avg = (graphql + npm + c_sharp + meang) / 4

# Comprobamos si hemos aprobado el curso (>= 5)
if (avg >= 5):
    print("¡¡Has aprobado!! Felicidades.")
else:
    print("No has aprobado. Intentalo de juevo el año que viene.")

print("================RESUMEN NOTAS================")
print(f"GraphQL: {graphql}")
print(f"NPM: {npm}")
print(f"C#: {c_sharp}")
print(f"MEAN+G: {meang}")
print("=============================================")
print("NOTA FINAL MEDIA: {}".format(avg))