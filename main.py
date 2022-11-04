class Számla:
    def __init__(self, name, account_number):
        self.tul_neve = name
        self.sz_szam = account_number
        self.egyenleg = 0

    def befizet(self, osszeg):
        self.egyenleg += osszeg

    def kivesz(self, osszeg):
        if osszeg > self.egyenleg:
            print("Nincs fedezet")
        else:
            self.egyenleg -= osszeg

    def lekerdez(self):
        return f'Your balance is {self.egyenleg}'


bank = dict()

while True:
    opc = int(input(
        "válassz a lehetőségek közül: 1:Számlanyitás, 2:Pénzbefizetés, 3:Pénzfelvétel, 4:Egyenleglekérdezés, 5:Kilépés"))
    if opc == 1:
        nev = input("adja meg a nevét")
        szamla = int(input("adja meg a számlaszámát"))
        bank[nev] = Számla(szamla, nev)
    elif opc == 2:
        szamla = int(input("adja meg a számlaszámát"))
        osszeg = int(input("adja meg a befizetni kívánt összeget"))
        bank[szamla].befizet(osszeg)
    elif opc == 3:
        szamla = int(input("adja meg a számlaszámát"))
        osszeg = int(input("adja meg a befizetni kívánt összeget"))
        bank[szamla].kivesz(osszeg)
    elif opc == 4:
        szamla = int(input("adja meg a számlaszámát"))
        bank[szamla].lekerdez(osszeg)
    elif opc == 5:
        print("kilépés")
        break
    else:
        print("rossz válasz")
        break

