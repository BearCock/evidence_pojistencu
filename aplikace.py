from databanka import Databanka
import time as _time

databanka = Databanka()   #založí instanci třídy Evidence

class Aplikace:

    def __init__(self):
        pass

    # metoda vytiskne úvodní obrazovku
    def vytiskni_uvodni_obrazovku(self):
        print("________________________________________________")
        print("Evidence pojištěných")
        print("________________________________________________")


    def vyber_volbu(self):
        while True:
            print("Vyberte si akci:\n"
                "1 - Přidat nového pojištěnce\n"
                "2 - Vypsat všechny pojištěnce\n"
                "3 - Vyhledat pojištěnce\n"
                "4 - Konec")

            zadani_volby = input() #uživatel zadá volbu
            print()

            # volba 1
            if zadani_volby == "1":
                self.zkontroluj_zadani_noveho_uzivatele() # spustí se kontrola vstupních dat
                input("\nData byla uloženam, pokračujte stisknutím klávesy 'Enter'...\n")

            # volba 2
            elif zadani_volby == "2":
                databanka.vrat_seznam_pojistencu()
                input("\nPokračujte stisknutím klávesy 'Enter'...\n")

            # volba 3 + kontrola vstupních dat
            elif zadani_volby == "3":
                #kontrola, zda seznam obsahuje nějaké položky. pokud ne, uživatel není vyzván k zadání údajů
                if len(databanka.pojistenci) == 0:
                    print("Seznam pojištěnců je prázdný.\n")
                    print("\nPokračujte stisknutím klávesy 'Enter'...\n")
                else:
                    while True:
                        jmeno = input("Zadejte křestní jméno pojištěnce:\n")
                        if not jmeno.isalpha():
                            print("Křestní jméno musí obsahovat pouze písmena!\n")
                        else:
                            break
                    # kontrola, zda je zadání složeno pouze z písmen
                    while True:
                        prijmeni = input("Zadejte příjmení pojištence:\n")
                        if not prijmeni.isalpha():
                            print("Přijmení musí obsahovat pouze písmena!\n")
                        else:
                            break
                        
                    # pokud projdou vstupní data, spustí se vyhledávání
                    databanka.vyhledej_pojistence(jmeno, prijmeni)

                input("\nPokračujte stisknutím klávesy 'Enter'...\n")

                # volba 4
            elif zadani_volby == "4":
                print("Program bude ukončen, děkuji za použítí aplikace.\n"
                      "Created by Jiří Mareček, BearCock Technology 2023©")
                _time.sleep(2.5) # před ukončením aplikace uspí program na daný čas 
                break
            else:
                print("Neplatná volba\n")


    # metoda zkontroluje vstupní data od uživatele, zda odpovídají požadavkům
    def zkontroluj_zadani_noveho_uzivatele(self):
        # kontrola, zda je zadání složeno pouze z písmen
        while True:
            jmeno = input("Zadejte křestní jméno pojištěnce:\n")
            if not jmeno.isalpha():
                print("Křestní jméno musí obsahovat pouze písmena!\n")
            else:
                break
        # kontrola, zda je zadání složeno pouze z písmen
        while True:
            prijmeni = input("Zadejte příjmení pojištence:\n")
            if not prijmeni.isalpha():
                print("Přijmení musí obsahovat pouze písmena!\n")
            else:
                break
        # kontrola, zda je vek celé číslo a zda je větší než 0
        while True:
            vek = input("Zadejte věk pojištěnce:\n")
            if not vek.isdigit() or int(vek) <= 0:
                print("Věk pojištěnce musí být celé číslo větší než 0!\n")
            else:
                break
        # kontrola, zda je telefon složen z 9 čísel
        while True:
            telefon = input("Zadejte telefonní číslo pojištěnce:\n")
            if not telefon.isnumeric() or len(telefon) != 9:
                print("Telefon musí obsahovat devět čísel!\n")
            else:
                break

        #pokud projdou všechna data podmínkami,přířadí se do seznamu pojištěnců
        databanka.pridej_pojistence(jmeno, prijmeni, vek, telefon)
