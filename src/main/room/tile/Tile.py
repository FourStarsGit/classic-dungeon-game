import pygame
from src.main import settings as st

class Tile:
    # Class-level cache for tile images
    _image_cache = {}

    def __init__(self):
        self.image_path = None
        self.is_traversable = None

    def load(self):
        if self.image_path not in self._image_cache:
            img = pygame.image.load(self.image_path).convert_alpha()
            self._image_cache[self.image_path] = pygame.transform.scale(img, (st.TILE_SIZE, st.TILE_SIZE))
        return self._image_cache[self.image_path]
    
    def update(self):
        pass

class Wall(Tile):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/rock.png"
        self.is_traversable = False

class LibraryWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/library_wall.png"

class LibraryWallDown(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/library_wall_down.png"

class FenceHorizontalWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/fence_horizontal.png"

class FenceVerticalWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/fence_vertical.png"

class FenceTopLeftWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/fence_top_left.png"

class FenceTopRightWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/fence_top_right.png"

class FenceBottomRightWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/fence_bottom_right.png"

class FenceBottomLeftWall(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/fence_bottom_left.png"

class DungeonCorner(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/dungeon_corner.png"

class Pikachu(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/pikachu.png"

class Asterix(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/asterix.png"

class CrashBandicoot(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/crash_bandicoot.png"

class Ectoplasma(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/ectoplasma.png"

class Goku(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/goku.png"

class HarryPotter(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/harry_potter.png"

class Idefix(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/idefix.png"

class Obelix(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/obelix.png"

class SquidGame(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/squid_game.png"

class Cat(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/cat.png"

class Edwige(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/edwige.png"

class Yoshi(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/yoshi.png"

class Garfield(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/garfield.png"

class Tintin(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/tintin.png"

class Haddock(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/haddock.png"

class Tournesol(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/tournesol.png"

class Dupond1(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/dupond1.png"

class Dupond2(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/dupond2.png"

class Milou(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/milou.png"

class Charlie(Wall):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/charlie.png"


class Door(Tile):

    def __init__(self, up_or_down):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/door_closed.png"
        self.is_traversable = False
        self.up_or_down = up_or_down
        self.is_open = False if up_or_down == "UP" else True

    def update(self):
        if self.is_open:
            self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/door_opened.png"
            self.is_traversable = True
        else:
            self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/door_closed.png"
            self.is_traversable = False

class LiftTopLeft(Door):

    def __init__(self, up_or_down):
        super().__init__(up_or_down)
        self.is_traversable = True
        self.is_open = True
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/lift_top_left.png"

    def update(self):
        pass

class LiftTopRight(Door):

    def __init__(self, up_or_down):
        super().__init__(up_or_down)
        self.is_traversable = True
        self.is_open = True
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/lift_top_right.png"

    def update(self):
        pass



class Floor(Tile):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/floor.png"
        self.is_traversable = True

class WoodFloor(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/wood_floor.png"

class SnowFloor(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/snow_floor.png"

class DungeonFloor(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/dungeon_floor.png"

class LiftBottomLeft(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/lift_bottom_left.png"

class LiftBottomRight(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/lift_bottom_right.png"

class BedTopLeft(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/bed_top_left.png"

class BedTopRight(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/bed_top_right.png"

class BedBottomLeft(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/bed_bottom_left.png"

class BedBottomRight(Floor):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/bed_bottom_right.png"

class BlindtestTreasureTile(Tile):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/blindtest_treasure.png"
        self.is_traversable = False
        
class TitleGameTile(Tile):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/title_game.png"
        self.is_traversable = False

class SleepingManTile(Tile):

    def __init__(self):
        super().__init__()
        self.image_path = f"{st.SPRITE_BACKGROUND_PATH}/sleeping_man"
        self.is_traversable = False

    def load(self):
        if self.image_path not in self._image_cache:
            frames = []
            for i in range(1, 12):  # Load 11 frames
                frame_path = f"{self.image_path}/frame{i}.png"
                img = pygame.image.load(frame_path)
                scaled_frame = pygame.transform.scale(img, (st.TILE_SIZE, st.TILE_SIZE))
                frames.append(scaled_frame)
            self._image_cache[self.image_path] = frames
            self.current_frame = 0
        
        # Cycle through frames more slowly by only updating every 6th call
        if not hasattr(self, 'frame_counter'):
            self.frame_counter = 0
        self.frame_counter = (self.frame_counter + 1) % 6
        
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % len(self._image_cache[self.image_path])
        
        return self._image_cache[self.image_path][self.current_frame]
