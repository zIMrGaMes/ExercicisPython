def lector_frase():
    global frase
    frase = (input("Escribe una frase ")). lower()
def contador_vocales():
    vocal = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    vocales = 0
    for i in vocal:
        for j in frase:
            if (i==j):
                vocales += 1
    print("Hay", vocales, "vocales.")
lector_frase()
contador_vocales()