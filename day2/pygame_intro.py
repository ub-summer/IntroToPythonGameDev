import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

running = True

player_speed = 6
player_location = [500, 250]

bg_color = (40, 97, 38)

while running:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_location[1] = player_location[1] - player_speed
    if keys[pygame.K_a]:
        player_location[0] -= player_speed
    if keys[pygame.K_s]:
        player_location[1] += player_speed
    if keys[pygame.K_d]:
        player_location[0] += player_speed

    pygame.draw.circle(screen, (128, 255, 0), player_location, 30)
    pygame.draw.rect(screen, (85, 12, 24), pygame.rect.Rect(0, 600, 1080, 120))
        
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    

pygame.quit()
print("Game Closed")
