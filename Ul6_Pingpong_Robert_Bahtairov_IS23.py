import pygame
pygame.init()
 
#värv
lPink = [255, 102, 204]
textvarv = [150, 75, 0]
 
#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Ping Pong")
screen.fill(lPink)
clock = pygame.time.Clock()
ballposX, ballposY = 0, 0 #palli pos
padposX, padposY = 10, screenY/1.5 #alus pos
ballSpeedX = 5 #palli kiirus vasak parem
ballSpeedY = 5 #palli kiirus üles alla
padSpeedX = 6 #alus kiirus vasak parem
pygame.mixer.music.load('img/Lines of Code.mp3')#laeb muusika
pygame.mixer.music.play(-1)#kordab muusika


#pad
pad = pygame.Rect(10, screenY/1.5, 120, 20) #alus kuju,pos ja suurus
padImage = pygame.image.load("img/pad.png") #alus pild
padImage = pygame.transform.scale(padImage, [pad.width, pad.height])

#ball

ball = pygame.Rect(ballposX, ballposY, 20, 20) #palli kuju,pos ja suurus
ballImage = pygame.image.load("img/ball.png") #pall pild
ballImage = pygame.transform.scale(ballImage, [ball.width,ball.height])

score = 0 #skoor
font = pygame.font.Font(None, 36) #skoori font


gameover = False
while not gameover:
    clock.tick(60)
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        gameover = True

    elif event.type == pygame.KEYDOWN:#Kui vajutat nuppu alla
        if event.key == pygame.K_RIGHT:#parem klahv
            padSpeedX = 6
        elif event.key == pygame.K_LEFT:#vasak klahv
            padSpeedX = -6
    elif event.type == pygame.KEYUP:#lased nuppu lahti
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                padSpeedX = 0
      
    
    ball = pygame.Rect(ballposX, ballposY, 20, 20)
    screen.blit(ballImage,ball)
    
    #palli liikumine
    ballposX += ballSpeedX
    ballposY += ballSpeedY

    if ballposX > screenX-ballImage.get_rect().width or ballposX < 0:
        ballSpeedX = -ballSpeedX
 
    if ballposY > screenY-ballImage.get_rect().height or ballposY < 0:
        ballSpeedY = -ballSpeedY
        

    pad = pygame.Rect(padposX, screenY/1.5, 120, 20)
    screen.blit(padImage,pad)    
    #alus liikumine
    padposX += padSpeedX
    
    if padposX > screenX-padImage.get_rect().width or padposX < 0:
        padSpeedX = 0
        
    #kokkupõrke 
    if ball.colliderect(pad) and ballSpeedY > 0:
        ballSpeedY *= -1
        score += 1
    elif ballposY > screenY - ball.height:
        score -= 1

    scoreText = font.render(f'Skoor: {score}', True, textvarv) #skoor näitamine
    screen.blit(scoreText, (10, 10))

    if ballposY > screenY - ball.height :#kui pall jõuab alla peadab muusika ja sulgeb mängu
        pygame.mixer.music.stop()
        pygame.display.quit()
        pygame.quit()

    
     
    pygame.display.flip()
    screen.fill(lPink)
        
pygame.quit()