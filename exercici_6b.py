def calcula_preu_total(preu_menjar):

    iva = round((float(preu_menjar) * 0.1),2)
    propina = round((float(preu_menjar) * 0.1),2)
    Preu_total = round((float(preu_menjar) + float(iva) + float(propina)),2)

    print ("El preu del menjar es de : " +str("{0:.2f}".format(preu_menjar)) + "€")
    print ("El preu del IVA es de: " +str("{0:.2f}".format(iva)) + "€")
    print ("El preu de la propina es de: " +str("{0:.2f}".format(propina)) + "€")
    print ("El preu total es de: " +str("{0:.2f}".format(Preu_total)) + "€")

print("Elige el plato")
print("Pizza     6€")
print("Ensalada  4€")
print("Kebab     3€")
print("Salmón    8€")

num_ordre = (input("Escribe el nombre del plato "))
has_dish = True

if num_ordre == "Pizza":
    calcula_preu_total(6)
elif num_ordre == "Ensalada":
    calcula_preu_total(4)
elif num_ordre == "Kebab":
    calcula_preu_total(3)
elif num_ordre == "Salmón":
    calcula_preu_total(8)
elif num_ordre == "Salmon":
    calcula_preu_total(8)
elif num_ordre == "ensalada":
    calcula_preu_total(4)
elif num_ordre == "kebab":
    calcula_preu_total(3)
elif num_ordre == "salmón":
    calcula_preu_total(8)
elif num_ordre == "salmon":
    calcula_preu_total(8)
elif num_ordre == "pizza":
    calcula_preu_total(6)
elif num_ordre == "ENSALADA":
    calcula_preu_total(4)
elif num_ordre == "KEBAB":
    calcula_preu_total(3)
elif num_ordre == "SALMÓN":
    calcula_preu_total(8)
elif num_ordre == "SALMON":
    calcula_preu_total(8)
elif num_ordre == "PIZZA":
    calcula_preu_total(6)
else:
    print("Este plato no está en el menú.")
    has_dish = False