from src.main.Boss import Beetle
from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog

# ROOM 11
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
    TextBox("queen lily", "Bravo ! Les DÉMONS ne font pas le poids contre vous !"),
    TextBox("queen lily", "Vous allez devoir affronter votre ennemi juré ! Le GROS SCARABÉE !"),
    TextBox("queen lily", "Faites attention à sa couleur ! S'il est vert, alors il est vulnérable."),
    TextBox("queen lily", "S'il est rouge, fuyez pour ne pas perdre de points de vie (représentés par des coeurs en haut à gauche) !"),
    TextBox("queen lily", "Il sera plus résistant que le CAPITAINE FRACASSE !")
], st.MAP_SURFACE)

post_dialog = Dialog([
    TextBox("queen lily", "Félicitations !!! Vous avez éclaté le méchant GROS SCARABÉE !"),
    TextBox("queen lily", "Votre santé est restaurée et vous gagnez un coeur supplémentaire.")
], st.MAP_SURFACE)

RoomFloor5 = Room("gros scarabée", layout, st.MAP_SURFACE, 
    pre_dialog=pre_dialog, 
    post_dialog=post_dialog,
    boss=Beetle(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2, st.SCREEN),
    music=st.SPYRO_EPIC_SOUND)