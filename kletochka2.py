import pygame
import random


pygame.init()

ekraan_w = random.randint(400, 800)
ekraan_h = random.randint(300, 600)
valge = [255 , 255, 255]
pind = pygame.display.set_mode((ekraan_w, ekraan_h))
pygame.display.set_caption("Ruuduvõrk")
pind.fill(valge)
def joonista_ruudustik():
    y = 0
    while y < ekraan_h:
        x = 0 
        rea_h = 0

        while x < ekraan_w:
            ruudu_w = random.randint(20, 60)
            ruudu_h = random.randint(20, 60)
            if x + ruudu_w > ekraan_w:
                ruudu_w = ekraan_w - x
            if y + ruudu_h > ekraan_h:
                ruudu_h = ekraan_h - y

            varv = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            pygame.draw.rect(pind, varv, (x, y, ruudu_w, ruudu_h))
            pygame.draw.rect(pind, (0, 0, 0), (x, y, ruudu_w, ruudu_h), 1)
            x += ruudu_w
            rea_h = max(rea_h, ruudu_h)
        y += rea_h  


joonista_ruudustik()


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Выход из Pygame
pygame.quit()
