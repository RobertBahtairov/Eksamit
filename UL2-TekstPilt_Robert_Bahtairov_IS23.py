import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ul 2")
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("img/bg_shop.jpg") #Laeb tausta pilti
screen.blit(bg,[0,0])

seller = pygame.image.load("img/seller.png") #Laeb müüa pilti
seller = pygame.transform.scale(seller, [254, 254])
screen.blit(seller,[115,220])

chat = pygame.image.load("img/chat.png") #Laeb juttu mulli pilti
chat = pygame.transform.scale(chat, [280, 180])
screen.blit(chat,[280,110])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('gabriola'), 45) #Teksti font gabriola ja suurus 45
text = font.render("Yo, olen Robert B.", True, [255,255,255]) #Tekst
screen.blit(text, [300,175]) #Koordinaatid kuhu kuvab teksti 

pygame.display.flip()

from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()