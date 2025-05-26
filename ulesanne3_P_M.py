# import pygame, sys, random
# pygame.init()
# # pygame.mixer.init()

# # collect_m=pygame.mixer.Sound('collect.mp3')

# lBlue = [153, 204, 255]
# white = [255, 255, 255]
# red = [255, 0, 0]
# green = [0, 255, 0]
# grey=[100,100,100]


# width = 800
# height = 600
# screen = pygame.display.set_mode([width, height])
# pygame.display.set_caption("Liikuv mesilane")


# bee = pygame.image.load("bee.png")
# bee_pic = pygame.transform.scale(bee, (30, 30))
# bee_rect = bee_pic.get_rect()


# nurgad = [(0, 0),(width - bee_rect.width, 0),(0, height - bee_rect.height),(width - bee_rect.width, height - bee_rect.height)]
# bee_rect.topleft = random.choice(nurgad)



# lilled = []
# for _ in range(5):
#     x = random.randint(50, width - 50)
#     y = random.randint(50, height - 50)
#     lilled.append(pygame.Rect(x,y,30,30))

# takistused=[]
# for _ in range(5):
#     w=60
#     h=10
#     x = random.randint(50, width - w)
#     y = random.randint(50, height - h)
#     takistused.append(pygame.Rect(x,y,w,h))

# while True:
#     bee_speed_x = random.choice([-3, 3])
#     bee_speed_y = random.choice([-3, 3])
#     if bee_speed_x != 0 and bee_speed_y != 0:
#         break

# def vastupäeva_liikumine():
#     bee_rect.x -= bee_speed_x
#     bee_rect.y -= bee_speed_y

# def päripäeva_liikumine():
#     bee_rect.x += bee_speed_x
#     bee_rect.y += bee_speed_y

# def diagonaalne_liikumine():
#     bee_rect.x += bee_speed_x
#     bee_rect.y -= bee_speed_y

# # liikumine = random.choice([vastupäeva_liikumine, päripäeva_liikumine, diagonaalne_liikumine])
# liikumine = diagonaalne_liikumine


# def joonista_mesilane():
#     screen.blit(bee_pic, bee_rect)


# def joonista_lilled():
#     for lill in lilled:
#         pygame.draw.circle(screen, lill['varv'], lill['pos'], lill['raadius'])

# def joonista_takistused():
#     for t in takistused:
#          pygame.draw.rect(screen,grey,t)

# clock = pygame.time.Clock()
# score = 0
# running = True

# while running:
#     screen.fill(lBlue)

#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # bee_rect.x *= bee_speed_x
#     # bee_rect.y *= bee_speed_y
#     liikumine()

#     if bee_rect.left <= 0 or bee_rect.right >= width:
#         bee_speed_x *= -1
#     if bee_rect.top <= 0 or bee_rect.bottom >= height:
#         bee_speed_y *= -1

#     for t in takistused:
#         if bee_rect.colliderect(t):
#             bee_speed_x *= -1
#             bee_speed_y*= -1
#             break

#     for lill in lilled:
#             if bee_rect.colliderect(lill):
#             lilled.remove(lill)
#             score += 1
#             # pygame.mixer.Sound.play(collect_m)


#     joonista_lilled()
#     joonista_mesilane()
#     joonista_takistused()

#     pygame.display.flip()
#     clock.tick(60)


#     print(score)
#     if score == 20:
#         running = False

# pygame.quit()

import pygame, sys, random
pygame.init()
# pygame.mixer.init()

# collect_m=pygame.mixer.Sound('collect.mp3')

lBlue = [153, 204, 255]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
grey=[100,100,100]


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
    lilled.append({'pos': (x, y), 'raadius': 30, 'varv': red})

takistused=[]
for _ in range(5):
    w=60
    h=10
    x = random.randint(50, width - w)
    y = random.randint(50, height - h)
    takistused.append(pygame.Rect(x,y,w,h))
while True:
    bee_speed_x = random.choice([-3, 3])
    bee_speed_y = random.choice([-3, 3])
    if bee_speed_x != 0 and bee_speed_y != 0:
        break

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



def joonista_mesilane():
    screen.blit(bee_pic, bee_rect)


def joonista_lilled():
    for lill in lilled:
        pygame.draw.circle(screen, lill['varv'], lill['pos'], lill['raadius'])

def joonista_takistused():
    for t in takistused:
         pygame.draw.rect(screen,grey,t)

clock = pygame.time.Clock()
score = 0
running = True

while running:
    screen.fill(white)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    diagonaalne_liikumine()

    if bee_rect.left <= 0 or bee_rect.right >= width:
        bee_speed_x *= -1
    if bee_rect.top <= 0 or bee_rect.bottom >= height:
        bee_speed_y *= -1

    for t in takistused:
        if bee_rect.colliderect(t):
            bee_speed_x *= -1
            bee_speed_y*= -1
            break


    for lill in lilled[:]:
        dx = bee_rect.centerx - lill['pos'][0]
        dy = bee_rect.centery - lill['pos'][1]
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist < 30 + lill['raadius']:
            lilled.remove(lill)
            score += 1
            # pygame.mixer.Sound.play(collect_m)
        else:
            lill['varv'] = red

    joonista_lilled()
    joonista_mesilane()
    joonista_takistused()

    pygame.display.flip()
    clock.tick(60)


    print(score)
    if score == 20:
        gameover = True

pygame.quit()