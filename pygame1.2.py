import pygame

pygame.init()
ekraan = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Anastassia Mayba")
valge = (255, 255, 255)
must = (0, 0, 0)
orange = (255, 165, 0)
punane = (255, 0, 0)
ekraan.fill(must)

pygame.draw.circle(ekraan, valge, (150, 220), 40)  
pygame.draw.circle(ekraan, valge, (150, 150), 30)  
pygame.draw.circle(ekraan, valge, (150, 100), 20)   
pygame.draw.circle(ekraan, must, (142, 95), 3)
pygame.draw.circle(ekraan, must, (158, 95), 3)
pygame.draw.rect(ekraan, punane, (130, 70, 40, 10))  
pygame.draw.rect(ekraan, punane, (135, 50, 30, 20))  


pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
