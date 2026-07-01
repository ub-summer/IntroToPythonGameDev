import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

running = True
down = False

bg_color = (40, 97, 38)
screen.fill(bg_color)

while running:
    
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            down = False

    if down:
        pygame.draw.circle(screen, (255, 255, 0), pygame.mouse.get_pos(), 24, 4)
        
    pygame.display.flip()
    

pygame.quit()
