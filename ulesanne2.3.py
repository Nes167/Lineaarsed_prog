import pygame
import sys
import random

pygame.init()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Majake")
pind.fill(lGreen)

#functions
def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width, y-(3/4.0) * height), (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    lineThickness = 3
    pygame.draw.lines(screen, color, False, points, lineThickness)

def drawDoor(x, y, width, height, screen, color):
    door_width=width/4
    door_height=height/2
    door_x= x+(width-door_width)/2
    door_y= y-door_height
    points = [(door_x,y), (door_x,door_y), (door_x+door_width,door_y), (door_x+door_width, y),(door_x,y)]
    lineThickness = 3
    pygame.draw.lines(screen, color, False, points, lineThickness)

drawHouse(100,400,300,400,pind,red)
drawDoor(100, 400, 300, 400, pind, blue)
# drawWindow(100, 400, 300, 400, pind, pink)
# drawChimney(100, 400, 300, 400, pind, red)

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()
