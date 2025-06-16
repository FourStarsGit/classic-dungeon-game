from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog
from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.Enemy import EnemyType


# ROOM 6
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

dialog = Dialog([
    TextBox("queen lily", "Bienvenue dans la TOUR KARIN ma chère PRINCESSE !"),
    TextBox("queen lily", "Le PRINCE est retenu tout en haut de cette TOUR."),
    TextBox("queen lily", "Les méchants PAPIERS ADMINISTRATIFS ont toujours d'autres alliés que vous devez combattre !"),
    TextBox("queen lily", "Détruisez tous ces DÉMONS ! Ils sont un peu plus résistants que vos précédents ennemis, frappez-les un peu plus !")
], st.MAP_SURFACE)
RoomFloor0 = Room("Tour Karin", layout, st.MAP_SURFACE, pre_dialog=dialog, enemies_number=3, enemy_type=EnemyType.DEMON)