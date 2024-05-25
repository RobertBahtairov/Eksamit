# Robert Bahtairov IS23 (#* = Ise lisanud/Modifitseerinud)
import random, math, pygame
from pygame.locals import *
pygame.init()

counter = 0
# Hääled ja Muusika *

muusika = pygame.mixer.music.load('failid/Zander Noriega - Perpetual Tension.mp3')
muusika = pygame.mixer.music.play(-1)
muusika = pygame.mixer.music.set_volume(0.2)
eat = pygame.mixer.Sound('failid/eat.wav')
die = pygame.mixer.Sound('failid/die.wav')


#PEAMINE 

def main():

    showstartscreen = 1
    
    while 1:
        # KONSTANTID

        WINSIZE = [800,600]
        WHITE = [255,255,255]
        BLACK = [0,0,0]
        RED = [255,0,0]
        GREEN = [0,255,0]
        DGREEN = [2,48,32] #*
        BLUE = [0,0,255]
        BLOCKSIZE = [20,20]
        UP = 1
        DOWN = 3
        RIGHT = 2
        LEFT = 4
        MAXX = 760
        MINX = 20
        MAXY = 560
        MINY = 80
        SNAKESTEP = 20
        TRUE = 1
        FALSE = 0
        
        ######## MUUTUJAD

        direction = RIGHT # 1=üles,2=paremale,3=alla,4=vasakule
        snakexy = [300,400]
        snakelist = [[300,400],[280,400],[260,400]]
        counter = 0
        score = 0
        kirssonscreen = 0 #*
        #kirssxy = [0,0]
        newdirection = RIGHT
        snakedead = FALSE
        gameregulator = 6
        gamepaused = 0
        growsnake = 0  # lisatud, et kasvatada saba iga kord kahe võrra 
        snakegrowunit = 2 # lisatud, et kasvatada saba iga kord kahe võrra
        
        
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption('SNAKE') #*
        taust = pygame.image.load("failid/hein.png") #*
        taust = pygame.transform.scale(taust, [800,600])#*
        screen.blit(taust,[0,0])#*
        kirssimg = pygame.image.load("failid/kirss.png")#*
        kirssimg = pygame.transform.scale(kirssimg, BLOCKSIZE)#*
        

        # näita algusekraani
        
        if showstartscreen == TRUE:
            showstartscreen = FALSE

            s = [[180,120],[180,100],[160,100],[140,100],[120,100],[100,100],[100,120],[100,140],[100,160],[120,160],[140,160],[160,160],[180,160],[180,180],[180,200],[180,220],[160,220],[140,220],[120,220],[100,220],[100,200]]
            
            kirss = [100,200] #*
            
            
            
            screen.blit(kirssimg,kirss)#*
            pygame.display.flip()
            clock.tick(8)
            
            for e in s:#*
                pygame.draw.rect(screen,GREEN,Rect(e,BLOCKSIZE))
                pygame.display.flip()
                clock.tick(8)
                
            font = pygame.font.SysFont("arial", 64)
            text_surface = font.render("NAKE", True, GREEN)#*
            screen.blit(text_surface, (220,180))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Liiguda madu kasutades arrow keys ja proovi kirsse süüa", True, WHITE)#*
            screen.blit(text_surface, (50,300))
            text_surface = font.render("Hoia seintest eemale!", True, WHITE)#*
            screen.blit(text_surface, (50,350))
            text_surface = font.render("Vajuta S tähte mängu alustamiseks   - Vajuta Q mängu lõpetamiseks", True, WHITE)#*
            screen.blit(text_surface, (50,400))
            text_surface = font.render("Vajuta P pausi jaoks ja R, et edasi mängida millal iganes", True, WHITE)#*
            screen.blit(text_surface, (50,450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit()
                if pressed_keys[K_s]: break

                clock.tick(10)


        while not snakedead:

            # saa sisendsündmused 

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[K_LEFT]: newdirection = LEFT
            if pressed_keys[K_RIGHT]: newdirection = RIGHT
            if pressed_keys[K_UP]: newdirection = UP
            if pressed_keys[K_DOWN]: newdirection = DOWN
            if pressed_keys[K_q]: snakedead = TRUE
            if pressed_keys[K_p]: gamepaused = 1

            # oota siin, kui p-klahv on vajutatud, kuni p-klahv on uuesti vajutatud
            
            while gamepaused == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_r]:
                    gamepaused = 0 
                clock.tick(10)

            
            if gameregulator == 6:

                # veendume, et me ei saa liikuda vastassuunas

                if newdirection == LEFT and not direction == RIGHT:
                    direction = newdirection

                elif newdirection == RIGHT and not direction == LEFT:
                    direction = newdirection

                elif newdirection == UP and not direction == DOWN:
                    direction = newdirection

                elif newdirection == DOWN and not direction == UP:
                    direction = newdirection
                    
                # nüüd liigume madu vastavalt suunale
                # kui tabame seina, siis madu sureb
                                

                if direction == RIGHT:
                    snakexy[0] = snakexy[0] + SNAKESTEP
                    if snakexy[0] > MAXX:
                        snakedead = TRUE
                    
                elif direction == LEFT:
                    snakexy[0] = snakexy[0] - SNAKESTEP
                    if snakexy[0] < MINX:
                        snakedead = TRUE
                        
                elif direction == UP:
                    snakexy[1] = snakexy[1] - SNAKESTEP
                    if snakexy[1] < MINY:
                        snakedead = TRUE
                        
                elif direction == DOWN:
                    snakexy[1] = snakexy[1] + SNAKESTEP
                    if snakexy[1] > MAXY:
                        snakedead = TRUE

                ### kas madu läheb enda pealt üle
                                        
                if len(snakelist) > 3 and snakelist.count(snakexy) > 0: 
                    snakedead = TRUE
                

                        
                #### genereeri kirss juhuslikus positsioonis, kui ekraanil pole kirssi
                #### veendu, et kirss ei ilmuks madu positsioonile
                    
                if kirssonscreen == 0: #*
                    good = FALSE
                    while good == FALSE:
                        x = random.randrange(1,39)
                        y = random.randrange(5,29)
                        kirssxy = [int(x*SNAKESTEP),int(y*SNAKESTEP)]
                        if snakelist.count(kirssxy) == 0:
                            good = TRUE
                    kirssonscreen = 1

                #### lisa uue madu pea positsioon
                #### kui me oleme söönud kirsi, siis ei eemalda saba (kasvata madu)
                #### kui me pole kirssi söönud, siis eemalda saba (madu jääb sama suurusega)

                snakelist.insert(0,list(snakexy))
                if snakexy[0] == kirssxy[0] and snakexy[1] == kirssxy[1]:
                    kirssonscreen = 0
                    score = score + 1
                    growsnake = growsnake + 1
                    pygame.mixer.Sound.play(eat)#*
                elif growsnake > 0:
                    growsnake = growsnake + 1
                    if growsnake == snakegrowunit:
                        growsnake = 0
                        pygame.mixer.Sound.play(eat)#*
                else:
                    snakelist.pop()
                    
                

                gameregulator = 0


            #EKRAANI JOONISTAMINE
            
            # Puhasta ekraan
            screen.blit(taust,[0,0])#*
            
            #Joonista ekraani piirid
            #horisontaaljooned
            pygame.draw.line(screen,DGREEN,(0,9),(799,9),20)#*
            pygame.draw.line(screen,DGREEN,(0,590),(799,590),20)#*
            pygame.draw.line(screen,DGREEN,(0,69),(799,69),20)#*
            # vertikaaljooned
            pygame.draw.line(screen,DGREEN,(9,0),(9,599),20)#*
            pygame.draw.line(screen,DGREEN,(789,0),(789,599),20)#*
            
            # Prindi skoor
            font = pygame.font.SysFont("arial", 38)
            text_surface = font.render("SNAKE!          Skoor: " + str(score), True, GREEN)#*
            screen.blit(text_surface, (50,18))

            # Väljasta array elemendid ekraanile ruutudena (madu)
            for element in snakelist:
                pygame.draw.rect(screen,GREEN,Rect(element,BLOCKSIZE))#*

            # Joonista kirss
            kirss = pygame.draw.rect(screen,WHITE,Rect(kirssxy,[0,0]))  #*              
            screen.blit(kirssimg,kirss)#*

            # Värskenda ekraani, et näidata kõike, mida just muutsime
            pygame.display.flip()



            gameregulator = gameregulator + 1
            
            clock.tick(25)


        # kui madu on surnud, siis on mäng läbi
            
        if snakedead == TRUE:                       
            pygame.mixer.Sound.play(die)#*            
            screen.blit(taust,[0,0])#*
            font = pygame.font.SysFont("arial", 48)
            text_surface = font.render("GAME OVER", True, RED)#*
            screen.blit(text_surface, (250,200))
            text_surface = font.render("Sinu Skoor: " + str(score), True, WHITE)#*
            screen.blit(text_surface, (250,300))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Vajuta Q, et lahkuda", True, WHITE)#*
            screen.blit(text_surface, (300,400))
            text_surface = font.render("Vajuta N, et uuesti mängida", True, WHITE)#*
            screen.blit(text_surface, (275,450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit()
                if pressed_keys[K_n]: break
                

                clock.tick(10)
    
if __name__ == '__main__':
    main()
