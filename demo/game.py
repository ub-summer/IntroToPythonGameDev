# Stolen from the pygame homepage
import math
import random

# Example file showing a circle moving on screen
import pygame
from pygame import Vector2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((160, 120), flags=pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0
pygame.mixer.init()

ENEMY_SIZE = Vector2(8, 10)
PLAYER_SIZE = Vector2(13, 13)
BULLET_SIZE = Vector2(7, 4)
PLAYER_START_X = screen.get_width() / 2
PLAYER_START_Y = 100

player_pos = Vector2(PLAYER_START_X, PLAYER_START_Y)
player_dir = Vector2(1, 0)


enemies = []

projectiles = []
projectile_cooldown = 0

spawn_countdown = 0

def place_image(filename, pos):
    image = pygame.image.load(filename)
    screen.blit(image, pos)

def create_projectile(location, direction, speed):
    velocity = Vector2(direction.x * speed, direction.y * speed)
    projectiles.append((Vector2(location.x, location.y), velocity))

def check_circles(location_a, radius_a, location_b, radius_b):
    dist = math.sqrt((location_a.x - location_b.x) ** 2 + (location_a.y - location_b.y) ** 2)
    if dist < radius_a + radius_b:
        return True
    return False

def check_rect(location_a, dim_a, location_b, dim_b):
    if location_a.x + dim_a.x < location_b.x:
        return False
    if location_a.x > location_b.x + dim_b.x:
        return False
    if location_a.y + dim_a.y < location_b.y:
        return False
    if location_a.y > location_b.y + dim_b.y:
        return False
    return True

def create_enemy(pos):
    enemies.append({"position": pos, "alive": True})


# just for fun
evil_projectiles = []
def create_evil_projectile(pos):
    velocity = Vector2(player_pos.x - pos.x, player_pos.y - pos.y)
    if not velocity.is_normalized():
     velocity = velocity.normalize()
    velocity *= 2
    evil_projectiles.append((pos.copy(), velocity))

def play_sound(filename):
    # play mp3
    sound = pygame.mixer.Sound(filename)
    sound.play()

create_enemy(Vector2(20, 20))

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#cadc9f")

    # spawn in new enemies randomly
    if spawn_countdown == 0:
        create_enemy(Vector2(random.randint(20, 140), random.randint(4, 70)))
        spawn_countdown = random.uniform(0.1, 4)

    # handle enemies
    for enemy in enemies:
        pos = enemy["position"]

        # spawn their projectiles randomly
        if random.random() < 0.02:
            create_evil_projectile(pos)

        # check if enemy is touching player
        if check_rect(pos, ENEMY_SIZE, player_pos, PLAYER_SIZE):
            player_pos = Vector2(random.randint(20, 120), PLAYER_START_Y)
            play_sound("ahhhhh_cut.mp3")

        # check if projectile is hitting enemy
        for proj_location, proj_velocity in projectiles:
            if check_rect(proj_location, BULLET_SIZE, pos, ENEMY_SIZE):
                enemy["alive"] = False
                play_sound("ahhhhh_cut.mp3")

        if enemy["alive"]:
            place_image("cat_face.png", enemy["position"])


    # remove enemies that aren't alive
    new_enemies = []
    for enemy in enemies:
            if enemy["alive"]:
                new_enemies.append(enemy)
    enemies = new_enemies

    # handle evil projectiles. again just for fun
    for proj_location, proj_velocity in evil_projectiles:
        proj_location += proj_velocity
        img = pygame.image.load("bullet.png")
        img = pygame.transform.rotate(img, 270 + proj_velocity.angle)
        img = pygame.transform.flip(img, False, True)
        screen.blit(img, proj_location)

        # enemy projectile hits player
        if check_rect(proj_location, BULLET_SIZE, player_pos, PLAYER_SIZE):
            player_pos = Vector2(random.randint(20, 120), PLAYER_START_Y)
            play_sound("ahhhhh_cut.mp3")

    # move and draw projectiles
    for proj_location, proj_velocity in projectiles:
        proj_location += proj_velocity
        place_image("bullet.png", proj_location)

    # check user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 100 * dt
        player_dir.y = -1
        player_dir.x = 0
    if keys[pygame.K_s]:
        player_pos.y += 100 * dt
        player_dir.y = 1
        player_dir.x = 0
    if keys[pygame.K_a]:
        player_pos.x -= 100 * dt
        player_dir.y = 0
        player_dir.x = -1
    if keys[pygame.K_d]:
        player_pos.x += 100 * dt
        player_dir.y = 0
        player_dir.x = 1
    if keys[pygame.K_SPACE] and projectile_cooldown == 0:
        play_sound("twang_crush.mp3")
        create_projectile(player_pos, Vector2(0, -1), 10)
        projectile_cooldown = 0.5

    if player_pos.x + PLAYER_SIZE.x > screen.get_width():
        player_pos.x = screen.get_width() - PLAYER_SIZE.x
    if player_pos.y + PLAYER_SIZE.y > screen.get_height():
        player_pos.y = screen.get_height() - PLAYER_SIZE.x
    if player_pos.x < 0:
        player_pos.x = 0
    if player_pos.y < 0:
        player_pos.y = 0

    # place the player at their position
    place_image("player2.png", player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    projectile_cooldown = max(projectile_cooldown - dt, 0)
    spawn_countdown = max(spawn_countdown - dt, 0)

pygame.quit()