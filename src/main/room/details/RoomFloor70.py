from src.main.Boss import OldDemon
from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog

# ROOM 18
layout = [
    [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), Door("UP"), Door("UP"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), BedTopLeft(), BedTopRight(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), BedBottomLeft(), BedBottomRight(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), Door("DOWN"), Door("DOWN"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()]
]

pre_dialog = Dialog([
    TextBox("queen lily", "Le boss final se dresse devant vous PRINCESSE !"),
    TextBox("queen lily", "Il s'agit du VIEUX DÉMON !"),
    TextBox("queen lily", "Faites attention à sa couleur ! S'il est vert, alors il est vulnérable."),
    TextBox("queen lily", "S'il est rouge, fuyez pour ne pas perdre de points de vie !"),
    TextBox("queen lily", "Faites attention, il est très résistant !")
], st.MAP_SURFACE)

post_dialog = Dialog([
    TextBox("queen lily", "Bravooooooo PRINCESSE !!!!! Le VIEUX DÉMON est tombé avec tous les PAPIERS ADMINISTRATIFS !"),
    TextBox("queen lily", "Allez maintenant libérer le PRINCE !")
], st.MAP_SURFACE)

RoomFloor70 = Room("Chambre du démon", layout, st.MAP_SURFACE, 
    pre_dialog=pre_dialog, 
    post_dialog=post_dialog,
    boss=OldDemon(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2, st.SCREEN),
    music=st.SPYRO_EPIC_SOUND)