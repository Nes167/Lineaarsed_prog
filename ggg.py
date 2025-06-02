import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hunt püüab mune")

white = [255, 255, 255]
lblue = [50, 150, 200]

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

wolf_img = pygame.image.load("wolf.png")
wolf_img = pygame.transform.scale(wolf_img, (100, 100))

egg_img = pygame.image.load("white_egg.png")
egg_img = pygame.transform.scale(egg_img, (40, 50))

golden_egg_img = pygame.image.load("egg.png")
golden_egg_img = pygame.transform.scale(golden_egg_img, (40, 50))

bomb_img = pygame.image.load("bomba.png")
bomb_img = pygame.transform.scale(bomb_img, (40, 50))

taust=pygame.image.load("nebo.jpg")
taust=pygame.transform.scale(taust,(WIDTH,HEIGHT))
screen.blit(taust,(0,0))

catch_sound = pygame.mixer.Sound("collect.mp3")
bomb_sound = pygame.mixer.Sound("bomb.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.3)
catch_sound.set_volume(0.6)
bomb_sound.set_volume(0.7)
game_over_sound.set_volume(0.7)

wolf_x = WIDTH // 2
wolf_y = HEIGHT - 100
wolf_speed = 10
eggs = []
score = 0
lives = 3
game_over = False
game_started = False

spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1500)

def spawn_egg():
    x = random.randint(50, WIDTH - 50)
    egg_type = random.choices(["normal", "golden", "bomb"], weights=[80, 10, 10])[0]
    eggs.append({'x': x, 'y': 0, 'type': egg_type})

def draw_text(text, x, y, color=white):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

while True:
    screen.blit(taust,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                pygame.quit()
                sys.exit()
            if not game_started and event.key == pygame.K_SPACE:
                eggs = []
                score = 0
                lives = 3
                wolf_x = WIDTH // 2
                game_over = False
                game_started = True
                pygame.mixer.music.play(-1)
            if game_over and event.key == pygame.K_r:
                eggs = []
                score = 0
                lives = 3
                wolf_x = WIDTH // 2
                game_over = False
                game_started = True
                pygame.mixer.music.play(-1)
        if event.type == spawn_event and game_started and not game_over:
            spawn_egg()
    keys = pygame.key.get_pressed()
    if game_started and not game_over:
        if keys[pygame.K_LEFT]:
            wolf_x -= wolf_speed
        if keys[pygame.K_RIGHT]:
            wolf_x += wolf_speed
        wolf_x = max(0, min(WIDTH - wolf_img.get_width(), wolf_x))
        screen.blit(wolf_img, (wolf_x, wolf_y))
        for egg in eggs[:]:
            egg['y'] += 5
            if egg['type'] == 'normal':
                img = egg_img
            elif egg['type'] == 'golden':
                img = golden_egg_img
            elif egg['type'] == 'bomb':
                img = bomb_img
            screen.blit(img, (egg['x'], egg['y']))
            if wolf_y < egg['y'] + img.get_height() < wolf_y + 20:
                if wolf_x < egg['x'] < wolf_x + wolf_img.get_width():
                    if egg['type'] == 'normal':
                        catch_sound.play()
                        score += 1
                    elif egg['type'] == 'golden':
                        catch_sound.play()
                        score += 5
                    elif egg['type'] == 'bomb':
                        bomb_sound.play()
                        lives -= 1
                    eggs.remove(egg)
            elif egg['y'] > HEIGHT:
                if egg['type'] == 'normal':
                    bomb_sound.play()
                    lives -= 1
                eggs.remove(egg)
            if lives <= 0:
                game_over = True
                pygame.mixer.music.stop()
                game_over_sound.play()
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Lives: {lives}", WIDTH - 150, 10)
    elif not game_started:
        draw_text("Alustamiseks vajutage SPACE", WIDTH // 2 - 150, HEIGHT // 2 - 100)
        draw_text("Väljumiseks vajutage ESC", WIDTH // 2 - 150, HEIGHT // 2 - 60)
    elif game_over:
        draw_text("Game over!", WIDTH // 2 - 100, HEIGHT // 2 - 50)
        draw_text(f"Score: {score}", WIDTH // 2 - 50, HEIGHT // 2)
        draw_text("Vajuta R, uue mängi alustamiseks", WIDTH // 2 - 180, HEIGHT // 2 + 50)
    pygame.display.flip()
    clock.tick(60)

