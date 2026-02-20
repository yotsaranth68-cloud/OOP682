import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    def __init__(self, name, filename, x, y, rows=2, cols=3, width=34, height=56):
        super().__init__()
        self.name = name
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet.set_colorkey((207, 252, 252))
        self.row = 0
        self.col = 0
        self.elapsed_time = 0
        self.rect = pygame.Rect(x, y, width, height)
        self.sound = pygame.mixer.Sound('sara/swish-1.wav')

    def act(self):
        self.sound.play()

    def update(self, elapsed_time):
        self.elapsed_time += elapsed_time
        if self.elapsed_time > 100: # 30 FPS
            self.col = (self.col + 1) % 3
            if self.col == 0:
                self.row = (self.row + 1) % 2
            self.elapsed_time -= 100

    def left(self): self.rect.x -= 5
    def right(self): self.rect.x += 5
    def up(self): self.rect.y -= 5
    def down(self): self.rect.y += 5

    def draw(self, surface):
        frame = self.sheet.subsurface(
                    self.col * self.rect.width, 
                    self.row * self.rect.height, 
                    self.rect.width, self.rect.height)
        surface.blit(frame, self.rect)