import pygame, sys
pygame.init()
red = [255, 0, 0]#variable
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
screenX = 640 #screenseaded
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine_2")
screen.fill(lBlue)
clock = pygame.time.Clock()
ball = pygame.image.load("tomcat.png") #graafika laadimine
posX, posY = 0, 0 #kiirus ja asukoht
speedX, speedY = 3, 4
gameover = False
while not gameover:
    clock.tick(60)
    #mangusulgaminerist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    #pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))
    posX += speedX
    posY += speedY
    #kui puudub ääri, siis muudab suunda
    if posX > screenX-ball.get_rect().width or posX < 0:
        speedx = -speedX
    if posY > screenY-ball.get_rect().height or posY < 0:
        speedY = -speedY
    #graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit()
