import pygame
import sys
pygame.init() #To get Pygame running
#colors
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

ekraan = pygame.display.set_mode( (640, 480))
ekraan.fill( lGreen )
pygame.display.set_caption("First Game")

gameover = False

while not gameover:
    #Let's add pictures
    youWin = pygame.image.load("win.png")
    youWin = pygame.transform.scale(youWin, [300, 200])
    ekraan.blit(youWin, [180,100])
    pygame.display.flip()
    #closing the game from the cross
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
pygame.quit() #Shutting down Pygame