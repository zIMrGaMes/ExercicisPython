def calcula_preu_total(preu_menjar):

    iva = round((float(preu_menjar) * 0.1),2)
    propina = round((float(preu_menjar) * 0.1),2)
    Preu_total = round((float(preu_menjar) + float(iva) + float(propina)),2)

    print ("El preu del menjar es de : " +str("{0:.2f}".format(preu_menjar)) + "€")
    print ("El preu del IVA es de: " +str("{0:.2f}".format(iva)) + "€")
    print ("El preu de la propina es de: " +str("{0:.2f}".format(propina)) + "€")
    print ("El preu total es de: " +str("{0:.2f}".format(Preu_total)) + "€")

print("Elige el plato")
print("1. Pizza     6€")
print("2. Ensalada  4€")
print("3. Kebab     3€")
print("4. Salmón    8€")

num_ordre = int(input("Escribe el número del plato "))

if num_ordre == 1:
    calcula_preu_total(6)
elif num_ordre == 2:
    calcula_preu_total(4)
elif num_ordre == 3:
    calcula_preu_total(3)
elif num_ordre == 4:
    calcula_preu_total(8)
else:
    print("Este plato no está en el menú.")