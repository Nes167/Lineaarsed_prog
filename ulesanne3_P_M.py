import pygame, sys, random
pygame.init()


lBlue = [153, 204, 255]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Liikuv mesilane")


bee = pygame.image.load("bee.png")
bee_pic = pygame.transform.scale(bee, (30, 30))
bee_rect = bee_pic.get_rect()


nurgad = [(0, 0),(width - bee_rect.width, 0),(0, height - bee_rect.height),(width - bee_rect.width, height - bee_rect.height)]
bee_rect.topleft = random.choice(nurgad)

lilled = []
for _ in range(5):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    lilled.append({'pos': (x, y), 'raadius': 60, 'varv': red})

lillCounter = 0
totallilled = 20
score = 0


bee_speed_x = random.choice([-3,3])
bee_speed_y = random.choice([-3,3])

def vastupäeva_liikumine():
    bee_rect.x -= bee_speed_x
    bee_rect.y -= bee_speed_y

def päripäeva_liikumine():
    bee_rect.x += bee_speed_x
    bee_rect.y += bee_speed_y

def diagonaalne_liikumine():
    bee_rect.x += bee_speed_x
    bee_rect.y -= bee_speed_y

# liikumine = random.choice([vastupäeva_liikumine, päripäeva_liikumine, diagonaalne_liikumine])
liikumine = diagonaalne_liikumine

def joonista_mesilane():
    screen.blit(bee_pic, bee_rect)

def joonista_lilled():
    for lill in lilled:
        pygame.draw.circle(screen, lill['varv'], lill['pos'], lill['raadius'])

for lill in lilled[:]:
    if bee_pic.colliderect(lill):
        lilled.remove(lill)
        score += 1

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(white)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    liikumine()

    if bee_rect.left <= 0 or bee_rect.right >= width:
        bee_speed_x *= -1
    if bee_rect.top <= 0 or bee_rect.bottom >= height:
        bee_speed_y *= -1
    
    for lill in lilled:
        dx = bee_rect.centerx - lill['pos'][0]
        dy = bee_rect.centery - lill['pos'][1]
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist < 40 + lill['raadius']:
            lill['varv'] = green

    joonista_lilled()
    joonista_mesilane()

    pygame.display.flip()
    clock.tick(60)

    print(score)
    if score == 20:
        gameover = True
pygame.quit()