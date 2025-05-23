import pygame
import sys
import random

pygame.init()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
ekraan_w=1000
ekraan_h=650

pind=pygame.display.set_mode([ekraan_w,ekraan_h])
pygame.display.set_caption("Majake")
pind.fill(lGreen)

maja_w=ekraan_w *(1/3)
maja_h=ekraan_h * (1/2)
x=(ekraan_w - maja_w) /2
y=(ekraan_h + maja_h * (3/4)) /2 

def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width, y-(3/4.0) * height), (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
    lineThickness = 3
    pygame.draw.lines(screen, color, False, points, lineThickness)

def drawDoor(x, y, width, height, screen, color):
    door_w=width/4
    door_h=height/2
    door_x= x+(width-door_w)/2
    door_y= y-door_h
    points = [(door_x,y), (door_x,door_y), (door_x+door_w,door_y), (door_x+door_w, y),(door_x,y)]
    lineThickness = 3
    pygame.draw.lines(screen, color, False, points, lineThickness)

def drawWindow(x, y, width, height, screen, color):
    window_suurus = width / 5
    window_x=x+width *(1/6)
    window_y=y-height *(1/2)
    points=[(window_x, window_y),(window_x + window_suurus, window_y),(window_x + window_suurus, window_y + window_suurus),(window_x, window_y + window_suurus),(window_x, window_y)]
    lineThickness = 3
    pygame.draw.lines(screen, False, color, points, lineThickness)

def drawChimney(x, y, width, height, screen, color):
    chimney_w = width/10
    chimney_h = height/4
    chimney_x = x + width*(3/4)
    chimney_y =y-height-chimney_h+65
    points = [(chimney_x, chimney_y + chimney_h),(chimney_x, chimney_y),(chimney_x + chimney_w, chimney_y),(chimney_x + chimney_w, chimney_y + chimney_h),(chimney_x, chimney_y + chimney_h)]
    lineThickness = 3
    pygame.draw.lines(screen, False, color, points, lineThickness)

drawHouse(x,y,maja_w, maja_h,pind,red)
drawDoor(x, y, maja_w, maja_h, pind,blue)
drawWindow(x, y, maja_w, maja_h, pind,pink)
drawChimney(x, y, maja_w, maja_h, pind,red)

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()
