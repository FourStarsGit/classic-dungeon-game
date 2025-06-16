from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog
from src.main.room.Room import Room
from src.main.room.tile.Tile import *

# ROOM 3
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

dialog = Dialog([
    TextBox("queen lily", "Bravo !! Vous vous débrouillez très bien !"),
    TextBox("queen lily", "Continuez de vous défouler sur ces saletés de MAÏS !")
], st.MAP_SURFACE)
RoomPathStart = Room("Sur la route", layout, st.MAP_SURFACE, background_color=st.SNOW_COLOR, pre_dialog=dialog, enemies_number=4)