from src.main.Enemy import *
from src.main import settings as st
import pygame
from pygame.locals import Rect
import random
from src.main.room.tile.Tile import Door, BlindtestTreasureTile, SleepingManTile, TitleGameTile

class Room:
    # Class-level cache for room surfaces
    _room_surface_cache = {}

    def __init__(self, 
                 room_name, 
                 room_layout, 
                 map_surface,
                 background_color = st.BLACK,
                 enemies_number = 0,
                 enemy_type = EnemyType.MAIZE,
                 pre_dialog = None,
                 post_dialog = None,
                 boss = None,
                 music = st.SPYRO_THE_DRAGON_SOUND):
        
        self.room_name = room_name
        self.map_surface = map_surface
        self.room_layout = room_layout
        self.walls = []
        self.background_color = background_color
        self.enemies_number = enemies_number
        self.initial_enemies_number = enemies_number
        self.enemies = pygame.sprite.Group()
        self.enemy_type = enemy_type
        self.doors = []
        self.door_open = False
        self.pre_dialog = pre_dialog
        self.post_dialog = post_dialog
        self.pre_dialog_shown = pre_dialog is None
        self.post_dialog_shown = post_dialog is None
        self.has_boss = boss is not None
        self.boss = boss
        self.music = music
        self.active_explosions = []

        for row_idx, row in enumerate(self.room_layout):
            for col_idx, _ in enumerate(row):
                if not self.room_layout[row_idx][col_idx].is_traversable:
                    self.walls.append(Rect([col_idx * st.TILE_SIZE, row_idx * st.TILE_SIZE, st.TILE_SIZE, st.TILE_SIZE]))
                if isinstance(self.room_layout[row_idx][col_idx], Door):
                    self.doors.append(self.room_layout[row_idx][col_idx])

        self.has_blindtest_treasure = self.get_treasure_tiles() != []
        self.has_title_game = self.get_title_game_tiles() != []
        self.blindtest_treasure_complete = not self.has_blindtest_treasure
        self.title_game_complete = not self.has_title_game


    def draw(self, enemies_defeated):
        # Check if this room's surface is already cached
        if self.room_name not in self._room_surface_cache:
            # Create a new surface for this room
            room_surface = pygame.Surface((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
            room_surface.fill(self.background_color)
            
            # Draw the room layout onto the new surface
            for row_idx, row in enumerate(self.room_layout):
                for col_idx, tile in enumerate(row):
                    x, y = col_idx * st.TILE_SIZE, row_idx * st.TILE_SIZE
                    tile_rendered = tile.load()
                    #if isinstance(tile_rendered, GIFPygame):
                    #    tile_rendered.render(st.SCREEN, (x, y))
                    #else :
                    room_surface.blit(tile_rendered, (x, y))
            
            # Cache the rendered surface
            self._room_surface_cache[self.room_name] = room_surface
        
        # Blit the cached surface onto the map surface
        self.map_surface.blit(self._room_surface_cache[self.room_name], (0, 0))

        if not self.pre_dialog_shown and self.pre_dialog:
            if self.pre_dialog.draw():
                self.pre_dialog_shown = True
                self.pre_dialog = None
        else:
            # Spawn enemies in valid positions
            enemies_remaining = max(self.initial_enemies_number - enemies_defeated, 0)
            for _ in range(enemies_remaining):
                x, y = self.find_valid_spawn_position()
                enemy = self.get_enemy_by_type(x, y)
                self.enemies.add(enemy)

        if not self.post_dialog_shown and self.post_dialog and self.boss is None:
            if self.post_dialog.draw():
                self.post_dialog_shown = True
                self.post_dialog = None

    def get_enemy_by_type(self, x, y):
        match self.enemy_type:
            case EnemyType.MAIZE:
                return EnemyMaize(x, y, st.SCREEN)
            case EnemyType.DEMON:
                return EnemyDemon(x, y, st.SCREEN)
            case EnemyType.PAPER:
                return EnemyPaper(x, y, st.SCREEN)

    # Update enemy spawning to ensure they don't spawn on walls
    def find_valid_spawn_position(self):
        while True:
            x = random.randint(st.TILE_SIZE * 2, st.SCREEN_WIDTH - st.TILE_SIZE * 2)
            y = random.randint(st.TILE_SIZE * 2, st.SCREEN_HEIGHT - st.TILE_SIZE * 2)
            test_rect = pygame.Rect(x, y, st.TILE_SIZE, st.TILE_SIZE)
            
            # Check if position collides with any walls
            valid_position = True
            for wall in self.walls:
                if test_rect.colliderect(wall):
                    valid_position = False
                    break
                    
            if valid_position:
                return x, y
            
            
    def check_door_status(self, enemies_defeated):
        """
        Check if all enemies are defeated and update door status accordingly.
        """
        if (self.enemies_number <= 0 or enemies_defeated >= self.initial_enemies_number) \
            and self.boss is None\
            and self.blindtest_treasure_complete\
            and self.title_game_complete\
            and not self.door_open:
            
            for door in self.doors:
                door.is_open = True
                door.update()

            self.door_open = True
                
            # Clear the cache to force redraw with updated door states
            if self.room_name in self._room_surface_cache:
                del self._room_surface_cache[self.room_name]
                
            self.get_walls_from_layout()
            self.draw(enemies_defeated)

    def get_walls_from_layout(self):
        self.walls = []
        for row_idx, row in enumerate(self.room_layout):
            for col_idx, _ in enumerate(row):
                if not self.room_layout[row_idx][col_idx].is_traversable:
                    self.walls.append(Rect([col_idx * st.TILE_SIZE, row_idx * st.TILE_SIZE, st.TILE_SIZE, st.TILE_SIZE]))
        
        if self.has_boss and self.pre_dialog_shown:
            self.boss.spawn()
            
    def update(self):
        if not self.pre_dialog_shown and self.pre_dialog:
            self.pre_dialog.update()
        if self.door_open and not self.post_dialog_shown:
            self.post_dialog.update()

    def get_treasure_tiles(self):
        treasure_tiles = []
        for x, row in enumerate(self.room_layout):
            for y, tile in enumerate(row):
                if isinstance(tile, BlindtestTreasureTile):
                    treasure_tiles.append((tile, x, y))
        return treasure_tiles

    def get_title_game_tiles(self):
        tiles = []
        for x, row in enumerate(self.room_layout):
            for y, tile in enumerate(row):
                if isinstance(tile, TitleGameTile):
                    tiles.append((tile, x, y))
        return tiles

    def get_sleeping_man_tiles(self):
        tiles = []
        for x, row in enumerate(self.room_layout):
            for y, tile in enumerate(row):
                if isinstance(tile, SleepingManTile):
                    tiles.append((tile, x, y))
        return tiles