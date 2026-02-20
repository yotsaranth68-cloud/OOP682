import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
sara = pygame.image.load("sara/sara-cal1.png")
clock = pygame.time.Clock()
running = True
while running: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0))
    screen.blit(sara, (50, 30))
    screen.blit(text, (250, 230))
    pygame.display.update()
pygame.quit()