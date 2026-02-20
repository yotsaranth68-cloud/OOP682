import sys, os
import pygame

from chars.sara import Hero

class SaraAdventure(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.caption = 'Sara Adventure'
        self.hero = Hero('Sara', 'sara/sara-cal1.png', 50, 50)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        pygame.display.set_caption(self.caption)

    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw_text(self, text, position, color=(0,0,0)):
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, position)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: 
            self.hero.act()
            self.hero.left()
        if keys[pygame.K_RIGHT]: self.hero.right()
        if keys[pygame.K_UP]: self.hero.up()
        if keys[pygame.K_DOWN]: self.hero.down()

    def start(self):
        while True:
            self.handle_close()
            self.handle_input()
            elapsed_time = self.clock.tick(60)
            self.screen.fill((255, 255, 255))
            self.hero.update(elapsed_time)
            self.draw_text("Sara Adventure", (100, 100))
            self.hero.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = SaraAdventure()
    game.start()