import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

running = True

ball_start_height = 300
ball_location = [random.randint(0, screen.get_width()), ball_start_height]
ball_speed = 300
ball_velocity = [ball_speed, ball_speed]
ball_color = (245, 215, 227)
ball_radius = 20
if random.random() > 0.5:
    ball_velocity[0] *= -1

paddle_speed = 400
paddle_color = (245, 215, 227)
paddle_size = (150, 20)
paddle = pygame.Rect((screen.get_width() - paddle_size[0])/2, screen.get_height() - 30, paddle_size[0], paddle_size[1])

bg_color = [100, 100, 100]

brick_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255)]
bricks = []

rows = 5
columns = 12
for column in range(columns):
    for row in range(rows):
        width = screen.get_width() / columns
        height = 30
        bricks.append({"rect": pygame.Rect(column * width, row * height + 100, width-2, height-2), "color": brick_colors[row % len(brick_colors)]})
        

def collide_circle_rectangle(circle_center, circle_radius, circle_velocity, rectangle):
    if circle_center[0] + circle_radius < rectangle.left:
        return False
    if circle_center[0] - circle_radius > rectangle.right:
        return False
    if circle_center[1] + circle_radius < rectangle.top:
        return False
    if circle_center[1] - circle_radius > rectangle.bottom:
        return False

    dl = circle_center[0] + circle_radius - rectangle.left
    dr = rectangle.right - (circle_center[0] - circle_radius)
    dt = circle_center[1] + circle_radius - rectangle.top
    db = rectangle.bottom - (circle_center[1] - circle_radius)

    dx = min(dl, dr)
    dy = min(dt, db)
    
    if dx < dy:
        circle_velocity[0] *= -1
    else:
        circle_velocity[1] *= -1

    return True

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
        ball_location[0] = random.randint(0, screen.get_width())
        ball_location[1] = ball_start_height
        ball_velocity[0] = ball_speed
        ball_velocity[1] = ball_speed
        if random.random() > 0.5:
            ball_velocity[0] *= -1
        for i in range(3):
            bg_color[i] = bg_color[i] - 20
        if bg_color[0] < 0:
            if not bricks:
                print("YOU WIN!!")
            else:
                print("You lose")
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        paddle.x -= dt * paddle_speed
        if paddle.left < 0:
            paddle.x = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        paddle.x += dt * paddle_speed
        if paddle.right > screen.get_width():
            paddle.x = screen.get_width() - paddle.width

    collide_circle_rectangle(ball_location, ball_radius, ball_velocity, paddle)

    for brick in bricks[:]:
        if collide_circle_rectangle(ball_location, ball_radius, ball_velocity, brick["rect"]):
            bricks.remove(brick)
            break

    pygame.draw.circle(screen, ball_color, ball_location, ball_radius)
    pygame.draw.rect(screen, paddle_color, paddle)    
    for brick in bricks:
        pygame.draw.rect(screen, brick["color"], brick["rect"])

    pygame.display.flip()


pygame.quit()
