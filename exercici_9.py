def calcula_precio_total(comida):

    IVA = round((float(comida) * 0.1),2)
    Propina = round((float(comida) * 0.1),2)
    precio_total = round((float(comida) + float(IVA) + float(Propina)),2)

    print("\nPrecio de la comida: " + str(float(comida)))
    print("IVA: " + str(float(IVA)))
    print("Propina: " + str(float(Propina)))
    print("Precio total: " + str(float(precio_total))+ "\n")

    return precio_total

num_personas = int(input("Quantes persones sou? "))

precio_total = 0
for i in range(num_personas):

    print("Tria el plato")
    print("1- Pizza    6€")
    print("2- Ensalada 4€")
    print("3- Kebab    3€")
    print("4- Salmón   8€")

    num_ordre = int(input("\n Escriu el número del menú: "))

    if num_ordre == 1:
        precio_plato = calcula_precio_total(6)
    elif num_ordre == 2:
        precio_plato = calcula_precio_total(4)

    elif num_ordre == 3:
        precio_plato = calcula_precio_total(3)
    elif num_ordre == 4:
        precio_plato = calcula_precio_total(8)
    else:
        print("El plato que has elegit no esta disponible.")
        precio_plato = 0

    precio_total = precio_total + precio_plato

print("EL precio total és " + str(round(precio_total,2)))