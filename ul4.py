class Lumi:
    def __init__(self, lumehelveste_arv):
        # Konstruktor, mis initsialiseerib lumehelveste arvu.
        self.lumehelveste_arv = lumehelveste_arv

    def __add__(self, n):
        # Ülekoormatud meetod liitmiseks.
        # Suurendab lumehelveste arvu n võrra.
        self.lumehelveste_arv += n
        return self

    def __sub__(self, n):
        # Ülekoormatud meetod lahutamiseks.
        # Vähendab lumehelveste arvu n võrra.
        self.lumehelveste_arv -= n
        return self

    def __mul__(self, n):
        # Ülekoormatud meetod korrutamiseks.
        # Korrutab lumehelveste arvu n-ga.
        self.lumehelveste_arv *= n
        return self

    def __truediv__(self, n):
        # Ülekoormatud meetod jagamiseks.
        # Jagab lumehelveste arvu n-ga ja ümardab tulemuse täisarvuks.
        self.lumehelveste_arv = int(self.lumehelveste_arv / n)
        return self

    def makeSnow(self):
        # Meetod, mis tagastab lumehelveste arvu põhjal moodustatud stringi.
        # Iga rida koosneb lumehelvestest, mille arv on võrdne lumehelveste arvuga.
        return "\n".join(["*" * self.lumehelveste_arv] * self.lumehelveste_arv)