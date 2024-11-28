#Dit bestand zal worden gebruikt als locale database, en zal worden aangeroepen in de functies van het programma

VoorraadItems = ['product 1', 'product 2']



def Voorraad():
    i = 0
    AantalItems = len(VoorraadItems)
    while(AantalItems > i ):
        print("Item nummer", i + 1, ":", VoorraadItems[i])
        i = i + 1


def VoorraadToevoegen(NieuwProduct):
    VoorraadItems.append(NieuwProduct)
    print(NieuwProduct, "is nu toegevoegd aan de inventaris op positie", len(NieuwProduct) - 1)


#uittesten

running1 = True
running2 = True

while running1 == True:

    print("1: Geef vooraad weer")
    print("2: Voeg item toe")
    print("Maak een keuze:")
    keuze = input()

    if keuze == '1':
        Voorraad()
        print("Wilt u het menu afsluiten? Type ja als u wilt afsluiten, en type nee als u terug wilt naar het hoofdmenu.")
        beeindigen = input()
        if beeindigen == "ja":
            running1 = False
        
    elif keuze == '2':
        while running2 == True:
            NieuwProduct = input("Welk product wilt u toevoegen? Als u geen product wilt toevoegen schrijf dan cancel")
            if NieuwProduct == 'cancel':
                running2 = False
            else:
                VoorraadToevoegen(NieuwProduct)
                
        

    else:
        print("Invoer was onjuist, probeer opnieuw")