import pygame 

def paike():
    x=400
    y=0
    for i in range(50):
        x-=10
        y+=10
        if i in[10,100]:
            pygame.draw.line(ekraani_pind,kollane,(0,0),(x+i,y+i),5)
        else:
            pygame.draw.line(ekraani_pind,kollane,(0,0),(x,y),5)

def krug():
    x=400
    y=300
    i=2
    for k in range(16):
        i+=6
        pygame.draw.circle(ekraani_pind, lilla, (x, y),i,3)

def bee():
    pilt1=pygame.image.load("bee.png")
    pilt1=pygame.transform.scale(pilt1,(50,50))
    ekraani_pind.blit(pilt1,(400,180))

def oblako():
    pygame.draw.circle(ekraani_pind,hall,(600,200),60)
    pygame.draw.circle(ekraani_pind,hall,(550,150),50)

pygame.init()
kollane=[255,255,0]
white=[255,255,255]
hall=[128,128,128]
sinine=[0,0,255]
roheline=[0,255,0]
purple=[160,32,240,255]
lilla=[238,130,238,255]
pink=[255,50,230]
pruun=[139,69,19]

ekraani_pind=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame aken")
ekraani_pind.fill(sinine)

paike()

pygame.draw.rect(ekraani_pind,roheline,(0,400,800,300))
pygame.draw.circle(ekraani_pind,purple,(400,300),100)
pygame.draw.rect(ekraani_pind,pruun,(390,400,20,150))

krug()
bee()
oblako()





font=pygame.font.SysFont('Bodoni MT Black',70)
sõnum="Tere tulemast!"
teksti_lisamine=font.render(sõnum, True, white)
ekraani_pind.blit(teksti_lisamine,(350,50))

pygame.display.flip()

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()