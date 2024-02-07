import random

class sodalane:
    def __init__(self, nimi):
        self.nimi = nimi
        self.tervis = 100
    
    def taba(self, teine):
        print(f"{self.nimi} lõõb")
        teine.tervis -= 20
        print(f"{teine.nimi} tervis: {teine.tervis}")
        
sodalane1 = sodalane("Sõdalane 1")
sodalane2 = sodalane("Sõdalane 2")

while sodalane1.tervis > 0 and sodalane2.tervis > 0:
    tabaja = random.choice([sodalane1, sodalane2])
    kaitsja = sodalane2 if tabaja == sodalane1 else sodalane1
    tabaja.taba(kaitsja)

if sodalane1.tervis <= 0:
    print("Esimine võitis!")
elif sodalane2.tervis <= 0:
    print("Teine võitis!")
    