# map/map_loader.py
import json
import os
from .layer import MapLayer

def load_map(json_path: str) -> dict:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    tile_w = data.get('tile_width', 64)
    tile_h = data.get('tile_height', 64)
    layers = {}
    for layer_def in data.get('layers', []):
        name = layer_def['name']
        # Resolve tileset path relative to map.json
        tileset_path = os.path.join(os.path.dirname(json_path), layer_def['tileset'])
        grid = layer_def['grid']
        layers[name] = MapLayer(name, tileset_path, tile_w, tile_h, grid)
    return layers