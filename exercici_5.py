Precio = input ("Quant costa menjar en el restaurant? ")

P = int(Precio)

a = (P*0.1)
b = (P*0.1)

Preu_total = (P+a+b)

print ("El preu del menjar es de : " +str("{0:.2f}".format(P)) + "€")
print ("El preu del IVA es de: " +str("{0:.2f}".format(a)) + "€")
print ("El preu de la propina es de: " +str("{0:.2f}".format(b)) + "€")
print ("El preu total es de: " +str("{0:.2f}".format(Preu_total)) + "€")