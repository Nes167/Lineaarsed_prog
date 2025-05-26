##3.1. osa
import pygame
import sys
pygame.init()

#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock() #3 lisame kell
ball = pygame.image.load("tomcat.png") #graafika laadimine
posX, posY = 580, 400#kiirus ja asukoht
speedX = 1 #2 lisame samm
gameover = False

while not gameover:
    #fps
    clock.tick(60) #3 pause
#mangusulgaminerist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        #pildi lisamine ekraanile
        screen.blit(ball, (posX, posY))
        posX -= speedX #2 x koordinaadi muutmine ehk liigub vasakule
        #graafika kuvamine ekraanil
        pygame.display.flip()

pygame.quit()
