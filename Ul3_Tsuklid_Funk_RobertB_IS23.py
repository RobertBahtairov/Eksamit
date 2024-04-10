import pygame
import sys

def drawRuut(screen, ruuduSuurus, rida, veer, joonVarv): #Ruutu funktsioon
    for row in range(rida):
        for col in range(veer):
            pygame.draw.rect(screen, joonVarv, (col * ruuduSuurus, row * ruuduSuurus, ruuduSuurus, ruuduSuurus), 1)

def main(ruuduSuurus, rida, veer, joonVarv): #Põhi funktsioon
    pygame.init()
    
    screen = pygame.display.set_mode((640,480)) #Ekraani suurus
    pygame.display.set_caption("Tsüklid ja funktsioonid")
      
    running = True #Mängutsükkel
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((100, 100, 255))   #Tausta värv
       
        drawRuut(screen, ruuduSuurus, rida, veer, joonVarv) #Joonista ruudustik       
        pygame.display.flip()
    
    pygame.quit() #Lõpeta Pygame
    sys.exit()

if __name__ == "__main__": #Käivita programm
    ruuduSuurus = 20  #Ruudu suurus
    rida = 30  #Ridade arv
    veer = 33  #Veergude arv
    joonVarv = (255, 0, 0)  #Joone värv (RGB)
    
    main(ruuduSuurus, rida, veer, joonVarv) #Põhi funktsioon käivitub