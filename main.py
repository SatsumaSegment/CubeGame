import pygame
import sys
import random
import objects

# Initialize Pygame engine 
pygame.init()

# Set the screen size
SIZE = WIDTH, HEIGHT = (800, 600)
SCREEN = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Cubie")

# Set game frame limit
FPS = 60
FPS_CLOCK = pygame.time.Clock()

# Create some color variables
COLOR_BLUE = (0, 0, 200)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (200, 0, 0)

# Create a font
font = pygame.font.Font('freesansbold.ttf', 32)

# Create game varibles here
moving_right = False
moving_left = False
moving_up = False
moving_down = False
speed = 2
score = 0

ens = 1

food_x = random.randint(0, WIDTH-10)
food_y = random.randint(0, HEIGHT-10)
seconds = 10

intro = 0

dt = 0

# Create game objects here
player = objects.Player(SCREEN, COLOR_BLUE, 10, 10, 20, 20)
food = objects.Food(SCREEN, COLOR_WHITE, food_x, food_y, 10, 10)
enemies = []
for i in range(10):
    enemy = objects.Enemy(SCREEN, COLOR_RED, random.randint(50, WIDTH-30), random.randint(50, HEIGHT-30), 20, 20)
    enemies.append(enemy)

# Game loop
while True:
    # Draw to the screen
    SCREEN.fill(COLOR_BLACK)

    player.draw()

    for e in range(ens):
        enemies[e].draw()

    food.draw()

    if score >= 10:
        winner = "You Win!"
        text = font.render(winner, True, COLOR_WHITE)
        ens = 0
        info = "Press 'ESC' to exit or 'R' to replay"
        text3 = font.render(info, True, COLOR_WHITE)
        SCREEN.blit(text, (WIDTH/2 - font.size(winner)[0]/2, 20))
        SCREEN.blit(text3, (WIDTH/2 - font.size(info)[0]/2, HEIGHT/2))
    else:
        text = font.render(str(score), True, COLOR_WHITE)
        SCREEN.blit(text, (WIDTH/2 - len(str(score)), 20))

    if intro == 0:
        todo = "Try to get to 10 points..."
        text2 = font.render(todo, True, COLOR_WHITE)
        SCREEN.blit(text2, (WIDTH/2 - font.size(todo)[0]/2, HEIGHT/2))
    if dt > 60*3:
        intro = 1

    # Spawn food randomly
    if dt == 60*seconds:
        food_x = random.randint(0, WIDTH-10)
        food_y = random.randint(0, HEIGHT-10)
        food = objects.Food(SCREEN, COLOR_WHITE, food_x, food_y, 10, 10)
        food.draw()
        dt = 0

    # Look for events
    for event in pygame.event.get():
        # Exit game if 'X' is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Get key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_r:
                score = 0
                player.x = 30
                player.y = 30
                player.w = 20
                player.h = 20
                ens = 1
                dt = 0
                intro = 0
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Get key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False

    # Player movement
    if player.x + player.w < WIDTH:    
        if moving_right:
            player.update(player.x + speed, player.y)
    if player.x > 0:
        if moving_left:
            player.update(player.x - speed, player.y)
    if player.y > 0:
        if moving_up:
            player.update(player.x, player.y - speed)
    if player.y + player.h < HEIGHT:
        if moving_down:
            player.update(player.x, player.y + speed)

    # Enemy movement
    for e in range(ens):
        if enemies[e].x + enemies[e].w >= WIDTH:
            enemies[e].right = False
            enemies[e].left = True
        if enemies[e].x <= 0:
            enemies[e].left = False
            enemies[e].right = True
        enemies[e].direction()

    # Deal with player collisions
    for e in range(ens):         
        if player.collision(enemies[e].this):
            seconds = 10
            score = 0
            player.x = 30
            player.y = 30
            player.w = 20
            player.h = 20
            ens = 1

    if player.collision(food.this):
        if score < 10:
            food_x = random.randint(0, WIDTH-10)
            food_y = random.randint(0, HEIGHT-10)
            food = objects.Food(SCREEN, COLOR_WHITE, food_x, food_y, 10, 10)
            player.w += 10
            player.h += 10
            score += 1
            if ens < 10:
                ens += 1
            if seconds > 1:
                seconds -= 1
                dt = 0

    dt += 1

    # Update screen at desired frame-rate
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)

