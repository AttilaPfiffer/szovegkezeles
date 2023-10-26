def szepnapvan():
    szoveg: str = "Szép nap van!"

    """Írd ki a szöveg első karakterét"""

    print("1. ", szoveg[0])
    """Írd ki a szöveg második karakterét"""
    print("2. ", szoveg[1])
    """Írd ki a szöveg hosszát"""
    print("A hossz: ", len(szoveg))
    """Írd ki a szöveg utolsó karakterét"""
    print("utolsó ", szoveg[len(szoveg) - 1] )

    """Írd ki a szöveg karaktereit egymás alá betűnként"""
    i:int = 0
    while i < len(szoveg):
        print(szoveg[i])
        i += 1

def szovegkezeles():
    szoveg:str = "Ez egy teszt szöveg"
    print(szoveg)
    print(szoveg.upper())
    """Van-e a szövegben 'teszt' szöveg"""
    """A SZÖVEG változóban hol szerepel először a 'S' betű"""
    """Alakítsd át minden  szó kezdőbetüjét nagybetűssé"""
    """Cseréld ki a teszt szót 'Próba'-ra"""
    print("\n")
    kereses = szoveg.find("teszt")
    if kereses >= 0:
        print("Nincs benne 'teszt'!")
    print(kereses)
    print("\n")
    kereses2 = szoveg.index("s")
    print(kereses2)
    print("\n")
    szoveg2 = szoveg.title()
    print(szoveg2)
    print("\n")
    szoveg3 = szoveg.replace("teszt", "próba")
    print(szoveg3)
    
def aszoveg_visszafele(szoveg:str):
    """A paraméterben kapott szöveg visszafele kiírva egymás mellé"""
    i:int = len(szoveg)
    while i != 0:
        print(szoveg[i-1], end = " ")
        i -= 1

def a_betuk_szama(szoveg:str):
    """Hány 'a' betű van a szövegben"""
    i:int = 0
    a_szam:int = 0
    while i < len(szoveg):
        if szoveg[i] == 'a':
            a_szam += 1
        i += 1
    print("A betűk száma: ", a_szam)
