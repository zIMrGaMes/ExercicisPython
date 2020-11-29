from discord_webhook import DiscordWebhook

url_webhook = 'https://discord.com/api/webhooks/781926092578619392/_xORf9w3GPMUsaq7T27fXzWGN4kVcuo1RWj4AWPA8XRWYmhMIwsMI8O6casmGRmB3We9'

def print_discord(mensaje):
    webhook = DiscordWebhook(url=url_webhook, content=mensaje)
    webhook.execute()

def calcula_preu_total(preu_menjar):

    iva = round((float(preu_menjar) * 0.1),2)
    propina = round((float(preu_menjar) * 0.1),2)
    Preu_total = round((float(preu_menjar) + float(iva) + float(propina)),2)

    print_discord ("El preu del menjar es de : " +str("{0:.2f}".format(preu_menjar)) + "€")
    print_discord ("El preu del IVA es de: " +str("{0:.2f}".format(iva)) + "€")
    print_discord ("El preu de la propina es de: " +str("{0:.2f}".format(propina)) + "€")
    print_discord ("El preu total es de: " +str("{0:.2f}".format(Preu_total)) + "€")

print_discord("Elige el plato")
print_discord("1. Pizza     6€")
print_discord("2. Ensalada  4€")
print_discord("3. Kebab     3€")
print_discord("4. Salmón    8€")

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
    print_discord("Este plato no está en el menú.")