# Robert Bahtairov IS23 (#* = Ise lisanud/Modifitseerinud) Ise lisanud- 5 asja
import random, math, pygame, time #importib neid
from pygame.locals import * #importib neid
pygame.init() #init pygamei

counter = 0
# Hääled ja Muusika * Ise kõik lisanud

muusika = pygame.mixer.music.load('failid/Zander Noriega - Perpetual Tension.mp3')#Tausta muusika
muusika = pygame.mixer.music.play(-1)#Muusika mängib lõppmatusi
muusika = pygame.mixer.music.set_volume(0.2)#Muusika vaiksemaks tegemine
eat = pygame.mixer.Sound('failid/eat.wav')#söömis hääl
die = pygame.mixer.Sound('failid/die.wav')#Surma hääl


#PEAMINE 

def main():

    showstartscreen = 1 #start screen tõene
    
    while 1:
        # KONSTANTID
        screenX=800
        screenY=600
        WINSIZE = [screenX,screenY]#ekraani suurus
        WHITE = [255,255,255]# Värv
        BLACK = [0,0,0]# Värv
        RED = [255,0,0]# Värv
        GREEN = [0,255,0]# Värv
        DGREEN = [2,48,32] #* Tume roheline värv
        BLUE = [0,0,255]# Värv
        BLOCKSIZE = [20,20]#kirsi suurus
        UP = 1
        DOWN = 3
        RIGHT = 2
        LEFT = 4
        MAXX = 760 #Max x Kordi kus madu saab liiguda
        MINX = 20 # Min x Kordi kus madu saab liiguda
        MAXY = 560 #Max Y Kordi kus madu saab liiguda
        MINY = 80 #Min Y Kordi kus madu saab liiguda
        SNAKESTEP = 20 # Madu sammu suurus
        TRUE = 1
        FALSE = 0

        ######## MUUTUJAD

        direction = RIGHT # 1=üles,2=paremale,3=alla,4=vasakule; mis suunas vaatades madu algab
        snakexy = [300,400]# madu algus kordi
        snakelist = [[300,400],[280,400],[260,400]]
        counter = 0
        score = 0#skoor
        kirssonscreen = 0 #*
        #kirssxy = [0,0]
        newdirection = RIGHT
        snakedead = FALSE#kas madu on surnud
        gameregulator = 6
        gamepaused = 0 # kas mäng on pausis
        growsnake = 0  # lisatud, et kasvatada saba iga kord kahe võrra 
        snakegrowunit = 2 # lisatud, et kasvatada saba iga kord kahe võrra
        speedX, speedY = 0, 0
        directionX, directionY = 0, 0
        blockerposX, blockerposY = 20, 200
        
        blocker = pygame.Rect(blockerposX, blockerposY, 40, 20)
        blockerSpeedX = 3
        pygame.init()
        clock = pygame.time.Clock()#Mängu kell 
        screen = pygame.display.set_mode(WINSIZE)#ekraani suurus
        pygame.display.set_caption('SNAKE') #*Ise lisanud; mis programmi nimi on
        taust = pygame.image.load("failid/hein.png") #*Ise lisanud; laeb tausta pildi
        taust = pygame.transform.scale(taust, [800,600])#*Ise lisanud ; muudab tausta pildi suurust
        screen.blit(taust,[0,0])#*Ise lisanud ; Laeb tausta ekraanile
        blockerImage = pygame.image.load("failid/blocker.png")
        blockerImage = pygame.transform.scale(blockerImage, [40,20])
        kirssimg = pygame.image.load("failid/kirss.png")#*Ise lisanud; laeb kirsi pildi
        kirssimg = pygame.transform.scale(kirssimg, BLOCKSIZE)#*Ise lisanud; teeb kirsi suuruse blocky suuruseks
        startaeg = time.time()
        
        

        # näita algusekraani
        
        if showstartscreen == TRUE:#Algus ekraan kui tõsi
            showstartscreen = FALSE
                
            s = [[180,120],[180,100],[160,100],[140,100],[120,100],[100,100],[100,120],[100,140],[100,160],[120,160],[140,160],[160,160],[180,160],[180,180],[180,200],[180,220],[160,220],[140,220],[120,220],[100,220],[100,200]] #start screenil S tähe tegemine
            
            kirss = [100,200] #* Ise lisanud; kirsi asukoht start screenil
            
            
            
            screen.blit(kirssimg,kirss)#*Ise lisanud; Laeb start screenil kirsi
            pygame.display.flip()
            clock.tick(8)
            
            for e in s:#*
                pygame.draw.rect(screen,GREEN,Rect(e,BLOCKSIZE))
                pygame.display.flip()
                clock.tick(8)
                
            font = pygame.font.SysFont("arial", 64)# Text Font ja suurus
            text_surface = font.render("NAKE", True, GREEN)#* ; start screeni Snake tekst teine osa
            screen.blit(text_surface, (220,180))# Kus text on
            font = pygame.font.SysFont("arial", 24)# Text Font ja suurus
            text_surface = font.render("Liiguda madu kasutades arrow keys ja proovi kirsse süüa", True, WHITE)#*; start screeni text
            screen.blit(text_surface, (50,300))# Kus text on
            text_surface = font.render("Hoia seintest eemale!", True, WHITE)#* ; start screeni text
            screen.blit(text_surface, (50,350))# Kus text on
            text_surface = font.render("Vajuta S tähte mängu alustamiseks   - Vajuta Q mängu lõpetamiseks", True, WHITE)#*; start screeni text
            screen.blit(text_surface, (50,400))# Kus text on
            text_surface = font.render("Vajuta P pausi jaoks ja R, et edasi mängida millal iganes", True, WHITE)#*; start screeni text
            screen.blit(text_surface, (50,450))# Kus text on

            pygame.display.flip()
            while 1:#kui näitab start screeni
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit() # kui vajutad Q tähte väljub mängust
                if pressed_keys[K_s]: break # kui vajutad S tähte alustab mängu

                clock.tick(10) # mängu kiirus


        while not snakedead: # kui madu ei ole surnud siis teeb edasi
            
            # saa sisendsündmused 

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            aeg_time = str(time.time() - startaeg)
            aegsek = str(int(time.time() - startaeg))        
            pressed_keys = pygame.key.get_pressed() #kui vajutad nuppu siis teeb edasi
            
            if pressed_keys[K_LEFT]: newdirection = LEFT #muudab direktsiooni vasakule
            if pressed_keys[K_RIGHT]: newdirection = RIGHT #muudab direktsiooni paremale
            if pressed_keys[K_UP]: newdirection = UP #muudab direktsiooni üles
            if pressed_keys[K_DOWN]: newdirection = DOWN#muudab direktsiooni alla
            if pressed_keys[K_q]: snakedead = TRUE #kui vajutad q siis muudab mao surnuks ja lahkub mängust
            if pressed_keys[K_p]: gamepaused = 1 # Kui vajutad P pausib mängu

            # oota siin, kui p-klahv on vajutatud, kuni r-klahv on vajutatud
            
            while gamepaused == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_r]: # Unpause mängu
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
                                

                if direction == RIGHT: #Madu sureb kui läheb vastu paremad seina
                    snakexy[0] = snakexy[0] + SNAKESTEP
                    if snakexy[0] > MAXX:
                        snakedead = TRUE
                    
                elif direction == LEFT:#Madu sureb kui läheb vastu vasakut seina
                    snakexy[0] = snakexy[0] - SNAKESTEP
                    if snakexy[0] < MINX:
                        snakedead = TRUE
                        
                elif direction == UP:#Madu sureb kui läheb vastu ülemist seina
                    snakexy[1] = snakexy[1] - SNAKESTEP
                    if snakexy[1] < MINY:
                        snakedead = TRUE
                        
                elif direction == DOWN:#Madu sureb kui läheb vastu alumist seina
                    snakexy[1] = snakexy[1] + SNAKESTEP
                    if snakexy[1] > MAXY:
                        snakedead = TRUE

                ### kas madu läheb enda pealt üle
                                        
                if len(snakelist) > 3 and snakelist.count(snakexy) > 0: 
                    snakedead = TRUE
                

                        
                #### genereeri kirss juhuslikus positsioonis, kui ekraanil pole kirssi
                #### veendu, et kirss ei ilmuks madu positsioonile
                    
                if kirssonscreen == 0: #* #kui kirssi ei ole siis edasi
                    good = FALSE
                    while good == FALSE:
                        x = random.randrange(1,39) #suvaline x kord
                        y = random.randrange(5,29) #suvaline y kord
                        kirssxy = [int(x*SNAKESTEP),int(y*SNAKESTEP)]
                        if snakelist.count(kirssxy) == 0:
                            good = TRUE
                    kirssonscreen = 1 #kui kirss on

                #### lisa uue madu pea positsioon
                #### kui me oleme söönud kirsi, siis ei eemalda saba (kasvata madu)
                #### kui me pole kirssi söönud, siis eemalda saba (madu jääb sama suurusega)

                snakelist.insert(0,list(snakexy))
                if snakexy[0] == kirssxy[0] and snakexy[1] == kirssxy[1]:
                    kirssonscreen = 0
                    score = score + 1 # lisab skoorile punkti kui kirss on söödud
                    growsnake = growsnake + 1 # teeb mao suuremaks
                    pygame.mixer.Sound.play(eat)#*; kui kirsi sööb mängib hääld
                elif growsnake > 0:
                    growsnake = growsnake + 1
                    if growsnake == snakegrowunit:
                        growsnake = 0
                        pygame.mixer.Sound.play(eat)#* kui kirsi sööb mängib hääld
                else:
                    snakelist.pop()
                    
                

 
                gameregulator = 0


            #EKRAANI JOONISTAMINE
            
            # Puhasta ekraan
            screen.blit(taust,[0,0])#*Ise lisanud
            
                            #Blcoker
            blocker = pygame.Rect(blockerposX, blockerposY, 20, 20)
            screen.blit(blockerImage,blocker)
                
                #liikumine
            blockerposX += blockerSpeedX
                

            if blockerposX > screenX-blockerImage.get_rect().width or blockerposX < 0:
                blockerSpeedX = -blockerSpeedX
            
            #kokkupõrke 
            
              
        
            
            #Joonista ekraani piirid
            #horisontaaljooned
            pygame.draw.line(screen,DGREEN,(0,9),(799,9),20)#*
            pygame.draw.line(screen,DGREEN,(0,590),(799,590),20)#*
            pygame.draw.line(screen,DGREEN,(0,69),(799,69),20)#*
            # vertikaaljooned
            pygame.draw.line(screen,DGREEN,(9,0),(9,599),20)#*
            pygame.draw.line(screen,DGREEN,(789,0),(789,599),20)#*
            
            # Prindi skoor
            font = pygame.font.SysFont("arial", 38)# Text Font ja suurus
            text_surface = font.render("SNAKE!          Skoor: " + str(score), True, GREEN)#*; mängu sisene tekst
            screen.blit(text_surface, (50,18))# Text asukoht

            # Väljasta array elemendid ekraanile ruutudena (madu)
            for element in snakelist:
                pygame.draw.rect(screen,GREEN,Rect(element,BLOCKSIZE))#*

            # Joonista kirss
            kirss = pygame.draw.rect(screen,WHITE,Rect(kirssxy,[0,0]))  #*Ise lisanud              
            screen.blit(kirssimg,kirss)#*Ise lisanud
            
            font = pygame.font.SysFont("arial", 30)# Text Font ja suurus
            text_surface = font.render("Aeg: " + str(aegsek), True, GREEN)#*; mängu sisene tekst
            screen.blit(text_surface, (600,21))# Text asukoht
            
 
            # Värskenda ekraani, et näidata kõike, mida just muutsime
            pygame.display.flip()



            gameregulator = gameregulator + 1
            
            clock.tick(25)


        # kui madu on surnud, siis on mäng läbi
            
        if snakedead == TRUE: #kui madu on surnud                      
            pygame.mixer.Sound.play(die)#*; mängi surma hääl            
            screen.blit(taust,[0,0])#* Laeb tühja tausta
            font = pygame.font.SysFont("arial", 48)# Text Font ja suurus
            text_surface = font.render("GAME OVER", True, RED)#* Tekst
            screen.blit(text_surface, (250,200))# text kord
            text_surface = font.render("Sinu Skoor: " + str(score), True, WHITE)#*Tekst
            screen.blit(text_surface, (250,300))# text kord
            font = pygame.font.SysFont("arial", 24)# Text Font ja suurus
            text_surface = font.render("Vajuta Q, et lahkuda", True, WHITE)#*Tekst
            screen.blit(text_surface, (300,400))# text kord
            text_surface = font.render("Vajuta N, et uuesti mängida", True, WHITE)#*Tekst
            screen.blit(text_surface, (275,450))# text kord
            font = pygame.font.SysFont("arial", 35)# Text Font ja suurus
            text_surface = font.render("Aeg: " + str(aegsek), True, WHITE)#*; mängu sisene tekst
            screen.blit(text_surface, (320,355))# Text asukoht
            
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
