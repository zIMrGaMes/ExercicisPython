botella_menos_1l = input("Quantitat de botelles de un litre o menys ") 
botella_mas_1l = input("Quantitat de botelles de un litre o mes ") 

c = int(botella_menos_1l)  
c1 = int(botella_mas_1l)

b = c*0.10
b1 = c1*0.25

print ("Per les botelles de un litre o menys et tornaran " +str(b) + "€")
print ("Per les botelles de un litre o mes et tornaran " +str(b1) + "€")