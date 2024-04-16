import pygame
import random 
pygame.init()

red = [255, 0, 0] #Punane
green = [0, 255, 0] #Roheline
blue = [0, 0, 255] #Sinine
pink = [255, 153, 255]#Roosa
lGreen = [153, 255, 153]#Heleroheline

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 3")
screen.fill(lGreen)#Tausta värv

for i in range (1,10):
    x = random.randint(0, 620)
    y = random.randint(0, 460) 
    pygame.draw.rect(screen, red, [x, y, 20, 20])#Joonistab ruudud suvaliselt

def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width,y-(3/4.0) * height), 
        (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

drawHouse(100,400,300,200,screen, red)#Joonistab maja

pygame.display.flip()

from sys import exit
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    