import pygame
import sys
import os
import json

# Configuration
TILE_SIZE = 64
GRID_SIZE = 20
SCREEN_WIDTH = TILE_SIZE * GRID_SIZE
SCREEN_HEIGHT = SCREEN_WIDTH + 60 # Extra space for UI

# Map to edit (default to forest)
map_target = 'forest'
if len(sys.argv) > 1:
    map_target = sys.argv[1]

MAP_FILE = os.path.join('assets', 'maps', f'{map_target}_map.json')
TILESET_PATH = os.path.join('assets', 'maps', f'{map_target}_tileset.png')

class MapEditor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(f"Map Editor [{map_target}] - Wheel: Select, click: draw, S: save, 1-4: layers")
        
        try:
            self.tileset = pygame.image.load(TILESET_PATH).convert_alpha()
        except Exception as e:
            print(f"Error loading tileset: {e}")
            pygame.quit()
            sys.exit()
            
        self.tileset_width = self.tileset.get_width()
        self.tileset_cols = self.tileset_width // TILE_SIZE
        self.tileset_rows = self.tileset.get_height() // TILE_SIZE
        self.total_tiles = self.tileset_cols * self.tileset_rows
        
        self.layers = self.load_existing_map()
        self.current_layer_index = 0
        self.selected_tile = 0
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

    def load_existing_map(self):
        if os.path.exists(MAP_FILE):
            try:
                with open(MAP_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data['layers']
            except Exception as e:
                print(f"Error reading JSON: {e}")
        
        # Fallback empty map with required layers
        return [
            {"name": "grass", "tileset": "forest_tileset.png", "grid": [[0]*GRID_SIZE for _ in range(GRID_SIZE)]},
            {"name": "path", "tileset": "forest_tileset.png", "grid": [[-1]*GRID_SIZE for _ in range(GRID_SIZE)]},
            {"name": "decor", "tileset": "forest_tileset.png", "grid": [[-1]*GRID_SIZE for _ in range(GRID_SIZE)]},
            {"name": "water", "tileset": "forest_tileset.png", "grid": [[-1]*GRID_SIZE for _ in range(GRID_SIZE)]}
        ]

    def save_map(self):
        data = {"layers": self.layers}
        try:
            with open(MAP_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            print(f"Map saved to {MAP_FILE}")
        except Exception as e:
            print(f"Error saving map: {e}")

    def get_tile_surface(self, tile_index):
        if tile_index < 0: return None
        tx = (tile_index % self.tileset_cols) * TILE_SIZE
        ty = (tile_index // self.tileset_cols) * TILE_SIZE
        # Safe crop
        if ty + TILE_SIZE <= self.tileset.get_height():
            return self.tileset.subsurface((tx, ty, TILE_SIZE, TILE_SIZE))
        return None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEWHEEL:
                    self.selected_tile = (self.selected_tile + event.y) % self.total_tiles
                    if self.selected_tile < 0: self.selected_tile += self.total_tiles

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.save_map()
                    if event.key == pygame.K_1: self.current_layer_index = 0
                    if event.key == pygame.K_2: self.current_layer_index = 1
                    if event.key == pygame.K_3: self.current_layer_index = 2
                    if event.key == pygame.K_4: self.current_layer_index = 3

            mouse_pos = pygame.mouse.get_pos()
            grid_x = mouse_pos[0] // TILE_SIZE
            grid_y = mouse_pos[1] // TILE_SIZE
            
            if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]: # Left Click
                    self.layers[self.current_layer_index]['grid'][grid_y][grid_x] = self.selected_tile
                elif mouse_buttons[2]: # Right Click
                    self.layers[self.current_layer_index]['grid'][grid_y][grid_x] = -1

            self.screen.fill((30, 30, 30))
            
            # Draw game area
            pygame.draw.rect(self.screen, (0,0,0), (0, 0, GRID_SIZE*TILE_SIZE, GRID_SIZE*TILE_SIZE))
            
            for layer in self.layers:
                grid = layer['grid']
                for y in range(GRID_SIZE):
                    for x in range(GRID_SIZE):
                        tile = grid[y][x]
                        if tile != -1:
                            surf = self.get_tile_surface(tile)
                            if surf:
                                self.screen.blit(surf, (x * TILE_SIZE, y * TILE_SIZE))

            # Draw preview
            if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                preview = self.get_tile_surface(self.selected_tile)
                if preview:
                    p_surf = preview.copy()
                    p_surf.set_alpha(150)
                    self.screen.blit(p_surf, (grid_x * TILE_SIZE, grid_y * TILE_SIZE))
            
            # UI Area
            pygame.draw.rect(self.screen, (50, 50, 50), (0, SCREEN_WIDTH, SCREEN_WIDTH, 60))
            layer_name = self.layers[self.current_layer_index]['name']
            txt = self.font.render(f"LAYER: {layer_name} (1-4) | TILE: {self.selected_tile} | S: SAVE", True, (255,255,255))
            self.screen.blit(txt, (10, SCREEN_WIDTH + 10))
            
            # Draw current tile preview
            curr_tile = self.get_tile_surface(self.selected_tile)
            if curr_tile:
                pygame.draw.rect(self.screen, (255,255,255), (SCREEN_WIDTH - TILE_SIZE - 20, SCREEN_WIDTH + 10, TILE_SIZE+2, TILE_SIZE+2), 1)
                self.screen.blit(curr_tile, (SCREEN_WIDTH - TILE_SIZE - 19, SCREEN_WIDTH + 11))

            pygame.display.flip()
            self.clock.tick(30)

if __name__ == "__main__":
    editor = MapEditor()
    editor.run()