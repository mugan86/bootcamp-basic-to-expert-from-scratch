print("Notas obtenidas en los exámenes")
graphql = float(input("GraphQL: "))
npm = float(input("NPM: "))
c_sharp = float(input("C#: "))
meang = float(input("MEAN+G: "))

avg = (graphql + npm + c_sharp + meang) / 4

# Comprobamos si hemos aprobado el curso (>= 5)
if (avg >= 5):
    print("¡¡Has aprobado!! Felicidades.")
    if(avg >= 9):
        print("Matricula de honor. El año que viene GRATIS :)")
    elif(avg < 9 and avg >= 8):
        print("Te ha faltado muy poco para la matrícula. ;)")
    else:
        print("El año que viene si es posible a mejorar esa nota. ANIMOOOO")
elif (avg < 5 and avg >=4): # 4-5
    print("Tienes que hacer un trabajo para aprobar")
elif (avg < 4 and avg >=3): # 3-4
    print("Tienes que hacer un trabajo y un exámen extra para aprobar")
else:
    print("No has aprobado. Intentalo de nuevo el año que viene.")

print("================RESUMEN NOTAS================")
print(f"GraphQL: {graphql}")
print(f"NPM: {npm}")
print(f"C#: {c_sharp}")
print(f"MEAN+G: {meang}")
print("=============================================")
print("NOTA FINAL MEDIA: {}".format(avg))