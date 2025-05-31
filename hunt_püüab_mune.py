import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hunt püüab mune")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)

font=pygame.font.SysFont('Arial',36)
small_font=pygame.font.SysFont('Arial',24)

wolf_img=pygame.image.load("wolf.png")
wolf_img=pygame.transform.scale(wolf_img, (100, 100))

egg_img = pygame.image.load("white_egg.png")
egg_img = pygame.transform.scale(egg_img, (40, 50))

golden_egg_img = pygame.image.load("egg.png")
golden_egg_img = pygame.transform.scale(golden_egg_img, (40, 50))

bomb_img = pygame.image.load("bomba.png")
bomb_img = pygame.transform.scale(bomb_img, (40, 50))

catch_sound = pygame.mixer.Sound("catch.wav")
bomb_sound = pygame.mixer.Sound("bomb.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
sound_enabled = True

# Игровые переменные
class Game:
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.paused = False
        self.in_menu = True
        self.eggs = []
        self.bombs = []
        self.wolf_x = WIDTH // 2 - 40
        self.wolf_y = HEIGHT - 100
        self.wolf_speed = 8
        self.egg_speed = 3
        self.spawn_rate = 60 # кадры между появлением яиц
        self.frame_count = 0
        self.golden_chance=0.05

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

# Создаем экземпляр игры
game = Game()

# Функции игры
def spawn_egg():
    x = random.randint(20, WIDTH - 60)
    if random.random() < game.golden_chance:
        game.eggs.append({"x": x, "y": -50, "type": "golden"})
    else:
        game.eggs.append({"x": x, "y": -50, "type": "normal"})

def spawn_bomb():
    x = random.randint(20, WIDTH - 60)
    game.bombs.append({"x": x, "y": -50})

def draw_wolf():
    screen.blit(wolf_img, (game.wolf_x, game.wolf_y))

def draw_eggs():
    for egg in game.eggs:
        if egg["type"] == "golden":
            screen.blit(golden_egg_img, (egg["x"], egg["y"]))
        else:
            screen.blit(egg_img, (egg["x"], egg["y"]))

def draw_bombs():
    for bomb in game.bombs:
        screen.blit(bomb_img, (bomb["x"], bomb["y"]))

def update_objects():
# Обновление позиций яиц
    for egg in game.eggs[:]:
        egg["y"] += game.egg_speed
        if egg["y"] > HEIGHT:
            game.eggs.remove(egg)
            if egg["type"] == "normal":
                game.lives -= 1
                if game.lives <= 0:
                    game.game_over = True
                    if sound_enabled:
                        game_over_sound.play()

# Обновление позиций бомб
    for bomb in game.bombs[:]:
        bomb["y"] += game.egg_speed + 1
        if bomb["y"] > HEIGHT:
            game.bombs.remove(bomb)

def check_collisions():
    wolf_rect = pygame.Rect(game.wolf_x, game.wolf_y, 80, 80)

# Проверка столкновений с яйцами
    for egg in game.eggs[:]:
        egg_rect = pygame.Rect(egg["x"], egg["y"], 40, 50)
        if wolf_rect.colliderect(egg_rect):
            if egg["type"] == "golden":
                game.score += 3
            else:
                game.score += 1
            game.eggs.remove(egg)
            if sound_enabled:
                catch_sound.play()

# Проверка столкновений с бомбами
    for bomb in game.bombs[:]:
        bomb_rect = pygame.Rect(bomb["x"], bomb["y"], 40, 50)
        if wolf_rect.colliderect(bomb_rect):
            game.lives -= 1
            game.bombs.remove(bomb)
            if sound_enabled:
                bomb_sound.play()
            if game.lives <= 0:
                game.game_over = True
                if sound_enabled:
                    game_over_sound.play()

def update_difficulty():
    if game.score >= game.level * 20:
        game.level += 1
        game.egg_speed += 0.5
        game.spawn_rate = max(20, game.spawn_rate - 5)
        if game.level > 3:
            game.golden_chance = 0.15 # Увеличиваем шанс золотых яиц

def draw_hud():
    score_text = font.render(f"Score: {game.score}", True, WHITE)
    lives_text = font.render(f"Lives: {game.lives}", True, WHITE)
    level_text = font.render(f"Level: {game.level}", True, WHITE)
    screen.blit(score_text,(10,10))
    screen.blit(lives_text,(10,50))
    screen.blit(level_text,(10,90))

def draw_menu():
    title = font.render("HUNT PÜÜAB MUNE", True, WHITE)
    start_text = small_font.render("Alustamiseks vajutage SPACE", True, WHITE)
    exit_text = small_font.render("Väljumiseks vajutage ESC", True, WHITE)
    high_score_text = small_font.render(f"Rekord: {game.high_score}", True, WHITE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//3))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
    screen.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//2 + 50))
    screen.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//2 + 100))

def draw_game_over():
    game_over_text = font.render("Mäng on läbi", True, RED)
    score_text = font.render(f"Teie score: {game.score}", True, WHITE)
    high_score_text = font.render(f"Rekord: {max(game.score, game.high_score)}", True, GOLD)
    restart_text = small_font.render("Alustamiseks vajutage SPACE", True, WHITE)
    exit_text = small_font.render("Väljumiseks vajutage ESC", True, WHITE)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//3))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//2 + 50))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 120))
    screen.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//2 + 170))

def reset_game():
    game.score = 0
    game.lives = 3
    game.level = 1
    game.egg_speed = 3
    game.spawn_rate = 60
    game.eggs = []
    game.bombs = []
    game.game_over = False
    game.wolf_x = WIDTH // 2 - 40
    game.wolf_y = HEIGHT - 100

# Основной игровой цикл
clock = pygame.time.Clock()
if sound_enabled:
    pygame.mixer.music.play(-1) # Зацикливаем фоновую музыку

running = True
while running:
# Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game.in_menu:
                    running = False
                elif game.game_over:
                    game.in_menu = True
            elif event.key == pygame.K_SPACE:
                if game.in_menu:
                    game.in_menu = False
                    reset_game()
                elif game.game_over:
                    reset_game()
            elif event.key == pygame.K_p and not game.in_menu and not game.game_over:
                game.paused = not game.paused

    if game.in_menu:
        screen.fill(BLACK)
        draw_menu()

    elif game.game_over:
        screen.fill(BLACK)
        draw_game_over()
        if game.score > game.high_score:
            game.high_score = game.score
            game.save_high_score()

    else:
        if game.paused:
            screen.fill(BLACK)
            draw_wolf()
            draw_eggs()
            draw_bombs()
            draw_hud()
            pause_text = font.render("PAUSE", True, WHITE)
            screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
        else:
            # Управление
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and game.wolf_x > 0:
                game.wolf_x -= game.wolf_speed
            if keys[pygame.K_RIGHT] and game.wolf_x < WIDTH - 80:
                game.wolf_x += game.wolf_speed

            # Спавн объектов
            game.frame_count += 1
            if game.frame_count % game.spawn_rate == 0:
                spawn_egg()
                if game.level > 2 and random.random() < 0.3:
                    spawn_bomb()

            # Обновление логики
            update_objects()
            check_collisions()
            update_difficulty()

            # Отрисовка
            screen.fill(BLACK)
            draw_wolf()
            draw_eggs()
            draw_bombs()
            draw_hud()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
