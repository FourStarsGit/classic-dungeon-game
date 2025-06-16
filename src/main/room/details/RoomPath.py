from src.main.room.Room import Room
from src.main.room.tile.Tile import *

# ROOM 4
layout = [
    [FenceTopLeftWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), Door("UP"), Door("UP"), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceTopRightWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceVerticalWall(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), SnowFloor(), FenceVerticalWall()],
        [FenceBottomLeftWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), Door("DOWN"), Door("DOWN"), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceHorizontalWall(), FenceBottomRightWall()]
]
RoomPath = Room("On continue", layout, st.MAP_SURFACE, background_color=st.SNOW_COLOR, enemies_number=9)