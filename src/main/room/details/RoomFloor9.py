from src.main.Boss import Python
from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog

# ROOM 15
layout = [
    [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), Door("UP"), Door("UP"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), Door("DOWN"), Door("DOWN"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()]
]

pre_dialog = Dialog([
    TextBox("queen lily", "Un nouvel ennemi surpuissant va se dresser devant vous !"),
    TextBox("queen lily", "Il s'agit d'un serpent que vous connaissez bien ! C'est le PYTHON !"),
    TextBox("queen lily", "Faites attention à sa couleur ! S'il est vert, alors il est vulnérable."),
    TextBox("queen lily", "S'il est rouge, fuyez pour ne pas perdre de points de vie !")
], st.MAP_SURFACE)

post_dialog = Dialog([
    TextBox("queen lily", "Mais vous êtes trop forte !!! En plus maintenant vous savez même parler PYTHON (un équivalent de FOURCHELANGUE) !"),
    TextBox("queen lily", "Votre santé est restaurée et vous gagnez un coeur supplémentaire.")
], st.MAP_SURFACE)

RoomFloor9 = Room("LE PYTHON", layout, st.MAP_SURFACE, 
    pre_dialog=pre_dialog, 
    post_dialog=post_dialog,
    boss=Python(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2, st.SCREEN),
    music=st.SPYRO_EPIC_SOUND)