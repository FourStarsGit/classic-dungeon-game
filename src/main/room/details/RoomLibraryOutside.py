from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog
from src.main.room.Room import Room
from src.main.room.tile.Tile import *

# ROOM 2
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
    TextBox("queen lily", "Bravo PRINCESSE ! Vous avez réussi à sortir du lit !"), 
    TextBox("queen lily", "Brrrrrr brrrr ! Il fait au moins... -8000 ! Le plus difficile reste à faire !"),
    TextBox("queen lily", "Les méchants PAPIERS ADMINISTRATIFS ont plein d'alliés, notamment les méchants épis de MAÏS !"),
    TextBox("queen lily", "Appuyez sur la touche Espace pour les attaquer !"),
    TextBox("queen lily", "Ne vous inquiétez pas, ils sont innofensifs. Tuez-les tous pour passer à la salle suivante."),
], st.MAP_SURFACE)

RoomLibraryOutside = Room("Extérieur", layout, st.MAP_SURFACE, background_color=st.SNOW_COLOR, enemies_number=2, pre_dialog=dialog)