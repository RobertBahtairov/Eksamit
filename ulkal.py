import math
#Teeb klassi kalkulaator
class kalkulaator():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
#Liidab esimese numbri teiseka    
    def liida(self):
        return self.num1 + self.num2
 #Lahudab teise numbri esimesest   
    def lahuda(self):
        return self.num1 - self.num2
#Korrutab kaks sisestatud numbrid    
    def korruda(self):
        return self.num1 * self.num2
#Jagab kaks sisestatud numbrid    
    def jagamine(self):
        if self.num2 == 0:
            return "ei saa jagada 0ga"
#Astendab, astmes on teine sisestatud number        
    def aste(self,):
        return self.num1 ** num2
#Annab esimese sisestatud arvu ruutu    
    def ruut(self):
        return math.sqrt(num1)
#Teeb inputid esimes ja teise numbrile
num1 = int(input("Sisesta esimene number: "))          
num2 = int(input("Sisesta teine number: "))
#Lühendab kalkulaadori klass ainuld "kalk"-iks
kalk = kalkulaator(num1, num2)                         
while True:
    #Kuvab valikud mis saad kalkulaatoriga teha
    def menu():
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. aste\n6. Ruutjuure leidmine. ')
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    if valik == 1:
        print("Vastus: ",kalk.liida())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahuta())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korruda())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.aste())
        break
    elif valik == 6:
        print("Vastus: ",kalk.ruut())
        break
    elif valik == 0:
        print('Sisesta uuesti üks liitmise operaator')
        break