import pygame
import random
pygame.init()
valge = [255 , 255, 255]

ekraan_w=random.randint(400,800)
ekraan_h=random.randint(400,800)

pind=pygame.display.set_mode([ekraan_w,ekraan_h])
pygame.display.set_caption("Harjutamine")
pind.fill(valge)

def joonista_ruudustik(pind,ruudu_w,ruudu_h, read, veerud):
    for rida in range(read):
        for veerg in range(veerud):
            varv=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
            x=veerg*ruudu_w
            y=rida*ruudu_h
            pygame.draw.rect(pind, varv, (x, y, ruudu_w, ruudu_h))
            pygame.draw.rect(pind,varv,(x,y,ruudu_w, ruudu_k), 1)
ruudu_k=random.randint(10,50)
ruudu_l=random.randint(10,50)
read=ekraan_w//ruudu_l+1
veerud=ekraan_h//ruudu_k+1

joonista_ruudustik(pind,ruudu_k,ruudu_l,read,veerud)

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()
