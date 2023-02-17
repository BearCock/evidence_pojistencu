from pojistenec import Pojistenec

class Databanka:

    def __init__(self):
        self.pojistenci = []  # při vytvoření nové instance třídy bude vytvořen prázdný seznam pojištěnců

    # pokud zadání projde kontrolou, tato metoda vytvoří novou instanci třídy Pojistenec a uloží ji do seznamu pojistencu
    def pridej_pojistence(self, jmeno, prijmeni, vek, telefon):
        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)

    # metoda ověří, jestli seznam pojistencu není prázdný, následně ho projde a výpíše jeho obsah
    def vrat_seznam_pojistencu(self):
        if len(self.pojistenci) > 0:
            for pojistenec in self.pojistenci:
                print(pojistenec)
        else:
            print("Seznam pojištěnců je prázdný.\n")

    # metoda na základě vstupu vyhledá pojištěnce a pokud se shoduje jméno i příjmení, vrátí joho údaje
    def vyhledej_pojistence(self, jmeno, prijmeni):
        vyhledano = False
        for pojistenec in self.pojistenci:
            if pojistenec.jmeno == jmeno and prijmeni == prijmeni:
                print (f"\n{pojistenec}")
                vyhledano = True  # pokud jsou nalezena vyhladávaná data, nastaví se vyhledano na True
        if not vyhledano: # v případě, že cyklus nic nenajde, vyhledano zůstává na False a tím se splní if not vyhledano
            print("Pojištěnec nenalezen.\n")
