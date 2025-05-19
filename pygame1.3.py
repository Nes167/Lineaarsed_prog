import pygame

pygame.init()
ekraan=pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 1.3")
valge = (255, 255, 255)
must = (0, 0, 0)
taust=pygame.image.load("taust.jpg")
taust=pygame.transform.scale(taust,(640,480))
ekraan.blit(taust,(0,0))
bee=pygame.image.load("bee.png")
bee=pygame.transform.scale(bee,(50,50))
ekraan.blit(bee,(400,180))
speech=pygame.image.load("speech.png")
speech=pygame.transform.scale(speech,(50,50))
ekraan.blit(speech,(400,130))


font=pygame.font.SysFont('Arial',10)
sõnum="Tere!"
teksti_lisamine=font.render(sõnum, True, must)
ekraan.blit(teksti_lisamine,(415,142))


pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
