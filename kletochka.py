import pygame


pygame.init()
red = [255, 0, 0]
lGreen = [153, 255, 153]
ekraan_w=640
ekraan_h=480

pind=pygame.display.set_mode([ekraan_w,ekraan_h])
pygame.display.set_caption("Ruuduvõrk")
pind.fill(lGreen)

def ruudustik(pind,ruudu_w,ruudu_h, read, veerud, varv):
    varv=red
    for rida in range(read):
        for veerg in range(veerud):
            x=veerg*ruudu_w
            y=rida*ruudu_h
            pygame.draw.rect(pind,varv,(x,y,ruudu_w, ruudu_h), 1)

ruudustik(pind,20,20,24,32,red)

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()
