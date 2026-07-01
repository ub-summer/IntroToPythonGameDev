import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

running = True

bucket_speed = 750
bucket_color = (135, 0, 0)
bucket_size = (100, 80)
bucket = pygame.Rect((screen.get_width() - bucket_size[0])/2, screen.get_height() - bucket_size[1] - 10, bucket_size[0], bucket_size[1])

bg_color = [135, 206, 235]

all_fruit = []
fruit_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255)]
fruit_size = 30
fruit_speed = 200
fruit_spawn_time = 3
fruit_timer = 1 # spawn the first fruit early

score = 0
score_rect = pygame.Rect(10, 10, 0, 0)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    dt = clock.tick(60) / 1000
    fruit_timer -= dt

    if fruit_timer < 0:
        all_fruit.append({"rect": pygame.Rect(random.randint(0, screen.get_width()-fruit_size), -fruit_size, fruit_size, fruit_size), "color": fruit_colors[random.randint(0, len(fruit_colors) - 1)]})
        fruit_timer = fruit_spawn_time

    for fruit in all_fruit[:]:
        fruit["rect"].y += dt * fruit_speed
        if fruit["rect"].colliderect(bucket):
            score += 1
            fruit_spawn_time = max(fruit_spawn_time - 0.1, 0.3)
            all_fruit.remove(fruit)
        if fruit["rect"].y > screen.get_height():
            score = max(0, score - 1)
            fruit_spawn_time = min(fruit_spawn_time + 0.2, 3)
            all_fruit.remove(fruit)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        bucket.x -= dt * bucket_speed
        if bucket.left < 0:
            bucket.x = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        bucket.x += dt * bucket_speed
        if bucket.right > screen.get_width():
            bucket.x = screen.get_width() - bucket.width

    pygame.draw.rect(screen, bucket_color, bucket)
    pygame.draw.rect(screen, [0, 0, 0], bucket, 2) 

    for fruit in all_fruit:
        pygame.draw.rect(screen, fruit["color"], fruit["rect"])
        pygame.draw.rect(screen, [0, 0, 0], fruit["rect"], 2)


    text = font.render("score: " + str(score), False, (0, 0, 0))
    screen.blit(text, score_rect)

    pygame.display.flip()


pygame.quit()
print("Ended with score of: " + str(score))