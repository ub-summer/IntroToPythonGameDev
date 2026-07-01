import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

running = True

ball_location = [500, 250]
ball_speed = 300
ball_velocity = [ball_speed, ball_speed]

bg_color = (18, 78, 120)
ball_color = (242, 187, 5)
ball_radius = 50

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)
    
    dt = clock.tick(60) / 1000
    ball_location[0] += dt * ball_velocity[0]
    ball_location[1] += dt * ball_velocity[1]
    
    if ball_location[0] - ball_radius < 0:
        ball_location[0] = ball_radius
        ball_velocity[0] = ball_speed
    if ball_location[1] - ball_radius < 0:
        ball_location[1] = ball_radius
        ball_velocity[1] = ball_speed

    if ball_location[0] + ball_radius > screen.get_width():
        ball_location[0] = screen.get_width() - ball_radius
        ball_velocity[0] = -ball_speed
    if ball_location[1] + ball_radius > screen.get_height():
        ball_location[1] = screen.get_height() - ball_radius
        ball_velocity[1] = -ball_speed

    pygame.draw.circle(screen, ball_color, ball_location, ball_radius)
    
    pygame.display.flip()


pygame.quit()
