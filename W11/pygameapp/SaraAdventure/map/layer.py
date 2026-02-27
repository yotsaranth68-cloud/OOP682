# map/layer.py
import pygame
from typing import List, Tuple

class MapLayer:
    def __init__(self, name: str, tileset_path: str, tile_width: int, tile_height: int, grid: List[List[int]]):
        self.name = name
        self.tileset = pygame.image.load(tileset_path).convert_alpha()
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.grid = grid
        self.tileset_cols = self.tileset.get_width() // tile_width

    def get_tile(self, tx: int, ty: int) -> int:
        if 0 <= ty < len(self.grid) and 0 <= tx < len(self.grid[0]):
            return self.grid[ty][tx]
        return -1

    def draw(self, surface: pygame.Surface, offset: Tuple[int, int] = (0, 0)):
        ox, oy = offset
        for row_idx, row in enumerate(self.grid):
            for col_idx, tile_idx in enumerate(row):
                if tile_idx < 0:
                    continue
                ts_col = tile_idx % self.tileset_cols
                ts_row = tile_idx // self.tileset_cols
                tile_rect = pygame.Rect(
                    ts_col * self.tile_width,
                    ts_row * self.tile_height,
                    self.tile_width,
                    self.tile_height,
                )
                dest_pos = (ox + col_idx * self.tile_width, oy + row_idx * self.tile_height)
                surface.blit(self.tileset, dest_pos, tile_rect)