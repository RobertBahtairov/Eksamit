import random

class Bingokaard:
    def __init__(self):
        # Loo bingokaart (5x5 maatriks) juhuslike numbritega
        self.kaard = [[random.randint(1, 25) for _ in range(5)] for _ in range(5)]
        # Märgi keskmine ruut "FREE"
        self.kaard[2][2] = "FREE"

    def mark_number(self, number):
        # Märgi number kaardil, kui see leidub
        for row in self.kaard:
            if number in row:
                row[row.index(number)] = "X"

    def check_bingo(self):
        # Kontrolli, kas on bingo
        # Kontrolli ridade, veergude ja diagonaalide järgi
        for row in self.kaard:
            if all(cell == "X" for cell in row):
                return True
        for col in range(5):
            if all(self.kaard[row][col] == "X" for row in range(5)):
                return True
        if all(self.kaard[i][i] == "X" for i in range(5)) or all(self.kaard[i][4 - i] == "X" for i in range(5)):
            return True
        return False

# Loo kaks bingokaarti
kaard1 = Bingokaard()
kaard2 = Bingokaard()

# Mängi bingot
while True:
    ball = random.randint(1, 25)
    print("Uus bingopall:", ball)
    kaard1.mark_number(ball)
    kaard2.mark_number(ball)
    if kaard1.check_bingo():
        print("Bingo! Mängija 1 võidab!")
        break
    if kaard2.check_bingo():
        print("Bingo! Mängija 2 võidab!")
        break
