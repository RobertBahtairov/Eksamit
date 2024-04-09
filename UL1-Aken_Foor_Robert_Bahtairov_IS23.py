import pygame

screen=pygame.display.set_mode([300,450])#akna suurus
pygame.display.set_caption("Lumemees - Robert Bahtairov")#akna nimi


pygame.draw.circle(screen, [0, 255, 0], [150,210], 30, 300)#alumine tuli
pygame.draw.circle(screen, [255, 255, 80], [150,140], 30, 300)#keskmine tuli
pygame.draw.circle(screen, [255, 0, 0], [150,70], 30, 300)#ülemine tuli
pygame.draw.rect(screen, [255, 255, 255], [100, 30, 100, 230], 2)#valgusfoori korpus
pygame.draw.line(screen, [255,255,255], [150,260], [150,330], 2)#post
pygame.draw.polygon(screen, (255, 255, 255), ((105,345),(150,300),(195,345)))#valge alus
pygame.draw.polygon(screen, (90, 90, 255), ((130,320),(150,300),(170,320)))#sinine alus
pygame.draw.polygon(screen, (000, 000, 0), ((130,320),(120,330),(180,330),(170,320)))# must alus



pygame.display.flip()

from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                