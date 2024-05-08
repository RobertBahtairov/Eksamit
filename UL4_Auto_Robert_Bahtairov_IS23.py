import pygame, random, sys
pygame.init()

#ekraani seaded
bg = pygame.image.load("img/bg_rally.jpg") #Laeb tausta pilti
screen=pygame.display.set_mode([640,480]) #Seab ekraani suuruse
pygame.display.set_caption("Ul 4 auto")
screen.blit(bg,(0,0)) #Kuvab tausta pildi
clock = pygame.time.Clock()




#Lisame pildid


f1red = pygame.image.load("img/f1_red.png") #Laeb punase auto pilti
f1red = pygame.transform.scale(f1red, [50, 50]) #Muudab auto suurust
screen.blit(f1red,[295,380])
#kiirus ja asukoht
posX = 180
posY=random.randint(0,300)
speedY = 3

f1blue1 = pygame.image.load("img/f1_blue.png") #Laeb sinise auto pilti
f1blue1 = pygame.transform.scale(f1blue1, [50, 50]) #Muudab auto suurust

#kiirus ja asukoht
posX2= 400
posY2=random.randint(0,300)
speedY2 = 3



f1blue2 = pygame.image.load("img/f1_blue.png") #Laeb sinise auto pilti
f1blue2 = pygame.transform.scale(f1blue2, [50, 50]) #Muudab auto suurust

# Skoori muutuja
skoor_punkt = 0
font = pygame.font.Font(None, 36)


gameover = False
while not gameover:
    #fps
    clock.tick(60)
 #mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
       if i.type == pygame.quit:
           sys.exit()


    screen.blit(f1red,[295,380])
    screen.blit(f1blue2,(posX2,posY2))
    screen.blit(f1blue1,(posX,posY))
    
    posY += speedY
    posY2 += speedY2
    
    if posY > 480:
        posY = random.randint(-100, 0)
        skoor_punkt += 1  # Lisame skoorile punkte
    if posY2 > 480:
        posY2 = random.randint(-100, 0)
        skoor_punkt += 1  # Lisame skoorile punkte

    skoor = font.render("Skoor: " + str(skoor_punkt), True, (255, 255, 255)) #Loob skoori teksti
    screen.blit(skoor, (10, 10)) #Kuvab skoori teksti


    pygame.display.flip() #Värskendab ekraani
    screen.blit(bg,(0,0)) #Kuvab tausta pildi

pygame.quit()



