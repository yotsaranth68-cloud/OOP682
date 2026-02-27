import sys, os
import pygame

from chars.sara import Hero
from map.map_loader import load_map

class SaraAdventure(object):
    def __init__(self):
        pygame.init()
        # Constants for layout
        self.tile_size = 64
        self.map_width = 20
        self.map_height = 20
        self.screen_width = self.tile_size * self.map_width
        self.screen_height = self.tile_size * self.map_height
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.caption = 'Sara Adventure'
        pygame.display.set_caption(self.caption)
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        
        # Path to hero spritesheet
        self.hero_sprite_path = os.path.join('assets', 'sara', 'sara_spritesheet.png')
        
        # Initial state
        self.restart()

    def restart(self):
        self.map_name = 'forest'
        self.load_current_map()
        # Hero(name, filename, x, y, ...)
        # We might need to scale the hero or her start position too
        self.hero = Hero('Sara', self.hero_sprite_path, 64, 64)
        self.won = False
        self.dead = False

    def load_current_map(self):
        map_file = f'assets/maps/{self.map_name}_map.json'
        try:
            self.layers = load_map(map_file)
        except Exception as e:
            print(f"Error loading map {map_file}: {e}")
            self.layers = {}

    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw_text(self, text, position, color=(255, 255, 255)):
        # Shadow for visibility
        shadow = self.font.render(text, True, (0, 0, 0))
        surface = self.font.render(text, True, color)
        self.screen.blit(shadow, (position[0]+1, position[1]+1))
        self.screen.blit(surface, position)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if not self.won and not self.dead:
            # Simple movement
            if keys[pygame.K_LEFT]: self.hero.left()
            if keys[pygame.K_RIGHT]: self.hero.right()
            if keys[pygame.K_UP]: self.hero.up()
            if keys[pygame.K_DOWN]: self.hero.down()
        
        # Restart logic
        if (self.won or self.dead) and keys[pygame.K_r]:
            self.restart()

    def check_collisions(self):
        # Calculate grid position based on hero center
        tx = self.hero.rect.centerx // self.tile_size
        ty = self.hero.rect.centery // self.tile_size

        if self.map_name == 'forest':
            # Check water death
            if 'water' in self.layers:
                if self.layers['water'].get_tile(tx, ty) != -1:
                    self.dead = True
            
            # Warp to space (Portal/Gem area)
            if tx >= 16 and 9 <= ty <= 11:
                self.map_name = 'space'
                self.load_current_map()
                self.hero.rect.x = self.tile_size
        
        elif self.map_name == 'space' and not self.won:
            # Warp back to forest
            if tx <= 0:
                self.map_name = 'forest'
                self.load_current_map()
                self.hero.rect.x = self.tile_size
                self.hero.rect.y = 10 * self.tile_size
            
            # Check for victory (Trophy)
            if 'items' in self.layers:
                if self.layers['items'].get_tile(tx, ty) != -1:
                    self.won = True

    def start(self):
        while True:
            self.handle_close()
            self.handle_input()
            elapsed_time = self.clock.tick(60)
            
            self.screen.fill((0, 0, 0))
            
            # Layered rendering (order of priority)
            layer_order = ['grass', 'floor', 'stars', 'path', 'decor', 'water', 'items', 'portal']
            for layer_name in layer_order:
                if layer_name in self.layers:
                    self.layers[layer_name].draw(self.screen)
            
            if not self.won and not self.dead:
                self.check_collisions()
                self.hero.update(elapsed_time)
                self.hero.draw(self.screen)
            elif self.dead:
                self.draw_text("YOU DIED!", (250, 250), (255, 0, 0))
                self.draw_text("Press R to Restart", (240, 300))
            else:
                self.draw_text("CONGRATULATIONS!", (200, 250), (255, 215, 0))
                self.draw_text("Press R to Play Again", (220, 300))

            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = SaraAdventure()
    game.start()