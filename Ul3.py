class Isik:
    def __init__(self, eesnimi, perekonnanimi, kvalifikatsioon=1):
        self.eesnimi = eesnimi
        self.perekonnanimi = perekonnanimi
        self.kvalifikatsioon = kvalifikatsioon

    def info(self):
        return f"{self.eesnimi} {self.perekonnanimi}, Kvalifikatsioon: {self.kvalifikatsioon}"

    def __del__(self):
        print(f"Hüvasti,härra {self.eesnimi} {self.perekonnanimi}!")

# Loo kolm Isiku klassi objekti
isik1 = Isik("Peeter", "Progand", 3)
isik2 = Isik("Maarja", "Ull", 2)
isik3 = Isik("Mark", "Luu")

# Kuvame töötajate teave
print(isik1.info())
print(isik2.info())
print(isik3.info())

# Vallandame nõrgima lüli
del isik3

# Ootame kasutaja sisendit enne programmi lõpetamist
input("Vajuta Enter, et lõpetada")