import pygame
import random
pygame.init()
valge = [255 , 255, 255]

ekraan_w=random.randint(400,800)
ekraan_h=random.randint(400,800)

pind=pygame.display.set_mode([ekraan_w,ekraan_h])
pygame.display.set_caption("Ruuduvõrk")
pind.fill(valge)

def ruudustik(pind,ruudu_w,ruudu_h, veerud, read):
    for rida in range(read):
        for veerg in range(veerud):
            varv=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            x=veerg*ruudu_w
            y=rida*ruudu_h
            pygame.draw.rect(pind, varv, (x, y, ruudu_w, ruudu_h))
ruudu_w=random.randint(10,50)
ruudu_h=random.randint(10,50)
read=ekraan_w//ruudu_w+1
veerud=ekraan_h//ruudu_h+1

ruudustik(pind,ruudu_w,ruudu_h,read,veerud)

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()
