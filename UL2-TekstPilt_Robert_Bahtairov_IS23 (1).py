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

vikk = pygame.image.load("img/VIKK logo.png") #Laeb VIKKi logo
vikk = pygame.transform.scale(vikk, [250, 45])
screen.blit(vikk,[0,0])

tort = pygame.image.load("img/tort.png") #Laeb torti pilti
tort = pygame.transform.scale(tort, [60, 60])
screen.blit(tort,[340,240])

mook = pygame.image.load("img/mõõk.png") #Laeb mõõga pilti
mook = pygame.transform.scale(mook, [70, 100])
screen.blit(mook,[10,140])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('gabriola'), 45) #Teksti font gabriola ja suurus 45
text = font.render("Yo, olen Robert B.", True, [255,255,255]) #Tekst
screen.blit(text, [300,175]) #Koordinaatid kuhu kuvab teksti

font = pygame.font.Font(pygame.font.match_font('ariel'), 25) 
font.set_italic(True)
text = font.render("TULEVIK 2050", True, [50,50,255]) #Tekst
screen.blit(text, [50,50]) 

pygame.display.flip()

from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()