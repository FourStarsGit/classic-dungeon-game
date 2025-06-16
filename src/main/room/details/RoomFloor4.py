from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.Enemy import EnemyType


# ROOM 10
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

RoomFloor4 = Room("Etage 4", layout, st.MAP_SURFACE, enemies_number=10, enemy_type=EnemyType.DEMON)