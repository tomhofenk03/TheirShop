#Dit bestand zal worden gebruikt als locale database, en zal worden aangeroepen in de functies van het programma

VoorraadItems = ['product 1', 'product 2']

def Voorraad():
    AantalItems = len(VoorraadItems)
    i = 0

    while(AantalItems > i ):
        print("Item nummer", i + 1, ":", VoorraadItems[i])
        i = i + 1


def VoorraadToevoegen():
    print("test")


#uittesten

running = True

while running == True:

    print("1: Geef vooraad weer")
    print("2: Voeg item toe")
    keuze = input("Maak een keuze")

    if keuze == '1':
        Voorraad()
        beeindigen = input("wilt u het menu sluiten?")
        if beeindigen == "ja":
            running = False
        
    elif keuze == '2':
        VoorraadToevoegen()
        running = False

    else:
        print("Invoer was onjuist, probeer opnieuw")