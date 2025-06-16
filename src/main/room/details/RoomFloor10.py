from src.main.Boss import Python
from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog

# ROOM 16
layout = [
    [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), LiftTopLeft("UP"), LiftTopRight("UP"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), LiftBottomLeft(), LiftBottomRight(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonCorner()],
        [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), Door("DOWN"), Door("DOWN"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()]
]

pre_dialog = Dialog([
    TextBox("queen lily", "Cette salle est un peu spéciale. Aucun ennemi ne vous y attend, mais seulement une sorte d'ascenseur."),
    TextBox("queen lily", "On dit que pour utiliser ce raccourci et arriver en haut de la TOUR KARIN où se trouve le PRINCE, il faut utiliser LES COULOIRS DU TEMPS !"),
    TextBox("queen lily", "En passant la porte, hurlez ces paroles chère PRINCESSE : QUE TRÉPASSE SI JE FAIBLIS ! (on a un micro !)")
], st.MAP_SURFACE)

RoomFloor10 = Room("Ascenseur", layout, st.MAP_SURFACE, 
    pre_dialog=pre_dialog, 
    enemies_number=0)