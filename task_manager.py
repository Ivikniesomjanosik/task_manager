ukoly=[]

def hlavni_menu():
    volba=""
    while volba != "4":
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4):") 

        if volba == "1":
          pridat_ukol()
        elif volba == "2":
          zobrazit_ukoly()
        elif volba == "3":
          odstranit_ukol()
        elif volba == "4":
          print("Konec programu.")
        else: 
          print("Vstup mimo rozsah zadání")


def pridat_ukol():
   nazev = input("Zadejte název úkolu:") 
   while nazev == "":
       print("Pole nesmí být prázdné. Zadejte prosím název úkolu")
       nazev = input("Zadejte název úkolu:")

   popis = input("Zadejte popis úkolu:")
   while popis == "":
       print("Pole nesmí být prázdné. Zadejte prosím popis úkolu")
       popis = input("Zadejte popis úkolu:")

   ukol = {"nazev": nazev, "popis": popis}
   ukoly.append(ukol)
   print(f"Úkol {nazev} byl úspěšne přidán")

def zobrazit_ukoly():
   if ukoly == []:
      print("Seznam úkolů je prázdný.")
   else:
      for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}" ) 
      
def odstranit_ukol():
   zobrazit_ukoly()
   if ukoly == []:
      return
   try:
    cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit."))
   except ValueError: 
      print("Zadaná hodnota je neplatná")
      return
   if cislo_ukolu > len(ukoly) or cislo_ukolu <= 0:
      print("Neplatný rozsah úkolů")
      return
   index = cislo_ukolu - 1
   odstraneny_ukol = ukoly.pop(index)
   print(f"Úkol {odstraneny_ukol['nazev']} byl odstraněn.")
   
hlavni_menu()

 
