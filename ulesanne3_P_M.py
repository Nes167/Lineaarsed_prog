from string import whitespace
import pygame, sys, random
pygame.init()
lBlue = [153, 204, 255]
white=[255,255,255]
red = [255,0,0]
green=[0,255,0]
width = 800
height = 600
screen=pygame.display.set_mode([width, height])
pygame.display.set_caption("Liikuv mesilane")
screen.fill(lBlue)

bee = pygame.image.load("bee.png") #graafika laadimine
bee_pic=pygame.transform.scale(bee,(80,80))
bee_rect=bee_pic.get_rect()

gameover = False
bee_speed=3
coords = []#koordinaatide loomine ja lisamine massiivi
nurgad=[(0,0),(width - bee_rect.width, 0),(0, height - bee_rect.height),(width - bee_rect.width),(height - bee_rect.height)]
bee_rect.topleft=random.choice(nurgad)

lilled=[]
for _ in range (5):
    x = random.randint(50, width-50)
    y = random.randint(50, height-50)
    lilled.append({'pos':(x,y),'raadius':15,'varv':red})

def vastupäeva_liikumine():
    bee_rect.x -=bee_speed
    bee_rect.y -=bee_speed

def päripäeva_liikumine():
    bee_rect.x +=bee_speed
    bee_rect.y +=bee_speed

def diagonaalne_liikumine():
    bee_rect.x +=bee_speed
    bee_rect.y -=bee_speed

liikumine=random.choice([vastupäeva_liikumine,päripäeva_liikumine,diagonaalne_liikumine])

def joonista_mesilane():
    screen.blit(bee_pic,bee_rect)

def joonista_lilled():
    for lill in lilled:
        pygame.draw.circle(screen,lill['pos'],lill['raadius'],lill['varv'])

clock = pygame.time.Clock()
running=True

while running:
    screen.fill(white)
    for i in pygame.event.get():
        if i.type == pygame. QUIT:
            sys.exit()

    liikumine()

    if x > width-bee_pic.get_rect().width or x < 0:
        speedx = -bee_speed
    if y > height-bee_pic.get_rect().height or y < 0:
        bee_speed = -bee_speed

    joonista_mesilane()
    joonista_lilled()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()