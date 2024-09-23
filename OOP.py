import random

class Postava:
    def __init__(self, jmeno, zivoty, sek_zdroj):
        self.jmeno = jmeno
        self.zivoty = zivoty
        self.sek_zdroj = sek_zdroj

    def ubrat_zivoty(self, dmg):
        self.zivoty -= dmg
        print(f"{self.jmeno} ztratil {dmg} životů, zbývá {self.zivoty} životů.")

    def je_zivy(self):
        return self.zivoty > 0

class Bojovnik(Postava):
    def __init__(self, jmeno):
        super().__init__(jmeno, 120, 50)
        self.schopnosti = {
            1: ('Úder kopem', 20, 10),
            2: ('Obranný postoj', 0, 5),
            3: ('Drtivý úder', 30, 15)
        }

class Kouzelnik(Postava):
    def __init__(self, jmeno):
        super().__init__(jmeno, 100, 80)
        self.schopnosti = {
            1: ('Ohnivá koule', 25, 15),
            2: ('Magická bariéra', 0, 10),
            3: ('Bleskový útok', 40, 30)
        }

class Lukostrelec(Postava):
    def __init__(self, jmeno):
        super().__init__(jmeno, 110, 60)
        self.schopnosti = {
            1: ('Rychlý šíp', 15, 5),
            2: ('Přesný zásah', 25, 10),
            3: ('Výbušný šíp', 35, 20)
        }

class Nepritel(Lukostrelec):
    def __init__(self, jmeno):
        super().__init__(jmeno)

    def vybrat_schopnost(self):
        schopnost = random.choice(list(self.schopnosti.values()))
        return schopnost

class Hra:
    def __init__(self):
        self.hrac = None
        self.nepritel = Nepritel("Nepřátelský lukostřelec")  

    def vyber_povolani(self):
        print("Vyber povolání: ")
        print("1 - Bojovník")
        print("2 - Kouzelník")
        print("3 - Lukostřelec")
        volba = input("Vaše volba: ")

        if volba == "1":
            self.hrac = Bojovnik("Hrdina")
        elif volba == "2":
            self.hrac = Kouzelnik("Hrdina")
        elif volba == "3":
            self.hrac = Lukostrelec("Hrdina")
        else:
            print("Neplatná volba. Zkus to znovu.")
            self.vyber_povolani()

    def boj(self):
        while self.hrac.je_zivy() and self.nepritel.je_zivy():  
            print("\n=== Tvůj tah ===")
            print("Vyber schopnost:")
            for cislo, schopnost in self.hrac.schopnosti.items():
                print(f"{cislo} - {schopnost[0]}")
            volba_schopnosti = int(input("Tvoje volba: "))

            if volba_schopnosti in self.hrac.schopnosti:
                schopnost, dmg, sek_zdroj_cost = self.hrac.schopnosti[volba_schopnosti]
                if self.hrac.sek_zdroj >= sek_zdroj_cost:
                    self.hrac.sek_zdroj -= sek_zdroj_cost
                    print(f"Použil jsi {schopnost} a způsobil {dmg} poškození.")
                    self.nepritel.ubrat_zivoty(dmg)
                else:
                    print("Nemáš dostatek zdrojů!")
            else:
                print("Neplatná volba!")

            if not self.nepritel.je_zivy():
                print("Porazil jsi nepřítele!")
                break

            print("\n=== Nepřítel na tahu ===")
            schopnost, dmg, _ = self.nepritel.vybrat_schopnost()
            print(f"Nepřítel použil {schopnost} a způsobil ti {dmg} poškození.")
            self.hrac.ubrat_zivoty(dmg)

            if not self.hrac.je_zivy():
                print("Byl jsi poražen!")

def hrat():
    hra = Hra()
    hra.vyber_povolani()
    hra.boj()

if __name__ == "__main__":
    hrat()
