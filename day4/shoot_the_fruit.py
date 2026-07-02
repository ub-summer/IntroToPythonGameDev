import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

running = True

cannon_speed = 600
cannon_color = (47, 79, 79)
cannon_size = (30, 50)
cannon = pygame.Rect((screen.get_width() - cannon_size[0])/2, screen.get_height() - cannon_size[1] - 10, cannon_size[0], cannon_size[1])

all_projectiles = []
projectile_speed = 2000
projectile_size = (2, 20)
projectile_color = (255, 255, 255)
projectile_cooldown_time = 0.3
projectile_timer = 0

bg_color = [128, 0, 0]

all_fruit = []
fruit_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255)]
fruit_size = 50
fruit_speed = 200
fruit_spawn_time = 3
fruit_timer = 1 # spawn the first fruit early

lives = 3

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    dt = clock.tick(60) / 1000

    fruit_timer -= dt
    if fruit_timer < 0:
        all_fruit.append({"rect": pygame.Rect(random.randint(0, screen.get_width()-fruit_size), -fruit_size, fruit_size, fruit_size), "color": fruit_colors[random.randint(0, len(fruit_colors) - 1)]})
        fruit_spawn_time = max(0.5, fruit_spawn_time - 0.3)
        fruit_timer = fruit_spawn_time

    projectile_timer = max(0, projectile_timer - dt)

    for fruit in all_fruit:
        fruit["rect"].y += dt * fruit_speed
    
    for projectile in all_projectiles:
        projectile["rect"].y -= dt * projectile_speed

    for fruit in all_fruit[:]:
        for projectile in all_projectiles[:]:
            if fruit["rect"].colliderect(projectile["rect"]):
                all_fruit.remove(fruit)
                all_projectiles.remove(projectile)

        if fruit["rect"].colliderect(cannon) or fruit["rect"].y > screen.get_height():
            lives -= 1
            all_fruit.remove(fruit)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cannon.x -= dt * cannon_speed
        if cannon.left < 0:
            cannon.x = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cannon.x += dt * cannon_speed
        if cannon.right > screen.get_width():
            cannon.x = screen.get_width() - cannon.width
    if keys[pygame.K_SPACE]:
        if projectile_timer <= 0:
            x_location = cannon.x + cannon.width/2 - projectile_size[0]/2
            y_location = cannon.y
            width = projectile_size[0]
            height = projectile_size[1]
            all_projectiles.append({"rect": pygame.Rect(x_location, y_location, width, height)})
            projectile_timer = projectile_cooldown_time

    pygame.draw.rect(screen, cannon_color, cannon)
    pygame.draw.rect(screen, [0, 0, 0], cannon, 2) 

    for fruit in all_fruit:
        pygame.draw.rect(screen, fruit["color"], fruit["rect"])
        pygame.draw.rect(screen, [0, 0, 0], fruit["rect"], 2)

    for projectile in all_projectiles:
        pygame.draw.rect(screen, projectile_color, projectile["rect"])
        # pygame.draw.rect(screen, [0, 0, 0], projectile["rect"], 2)

    if lives > 0:
        text = font.render("lives: " + str(lives), False, (255, 255, 255))
        screen.blit(text, (10, 10))
    else:
        screen.fill((0, 0, 0))
        big_font = pygame.font.Font(None, 120)
        text = big_font.render("GAME OVER", False, (255, 255, 255))
        text_rect = text.get_rect()
        screen.blit(text, (screen.get_width()/2 - text_rect.width/2, screen.get_height()/2 - text_rect.height/2))

    pygame.display.flip()


pygame.quit()
print("Ended with score of: " + str(score))