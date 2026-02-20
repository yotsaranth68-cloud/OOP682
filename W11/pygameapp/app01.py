import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame 01")
running = True
while running: #game loop
    pygame.time.delay(100)
    pygame.display.update()
    