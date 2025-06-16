from src.main.room.Room import Room
from src.main.room.tile.Tile import *
from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog

# ROOM 19
layout = [
    [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()],
        [DungeonCorner(), Obelix(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), Haddock(), Pikachu(), DungeonCorner()],
        [DungeonCorner(), CrashBandicoot(), Idefix(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), Tintin(), Charlie(), Edwige(), DungeonCorner()],
        [DungeonCorner(), Garfield(), Charlie(), Asterix(), DungeonFloor(), DungeonFloor(), DungeonFloor(), Ectoplasma(), Yoshi(), HarryPotter(), Goku(), DungeonCorner()],
        [DungeonCorner(), Ectoplasma(), Pikachu(), DungeonFloor(), DungeonFloor(), SleepingManTile(), DungeonFloor(), DungeonFloor(), CrashBandicoot(), Garfield(), SquidGame(), DungeonCorner()],
        [DungeonCorner(), Dupond1(), Dupond2(), SquidGame(), DungeonFloor(), DungeonFloor(), DungeonFloor(), Cat(), Idefix(), Haddock(), Yoshi(), DungeonCorner()],
        [DungeonCorner(), Cat(), Goku(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), Edwige(), Milou(), Tintin(), DungeonCorner()],
        [DungeonCorner(), HarryPotter(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), DungeonFloor(), Tournesol(), Asterix(), DungeonCorner()],
        [DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), Door("DOWN"), Door("DOWN"), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner(), DungeonCorner()]
]

dialog = Dialog([
    TextBox("queen lily", "Regardez PRINCESSE ! Le PRINCE dort paisiblement."),
    TextBox("queen lily", "Autour, on voit énormément de peluches ! Regardez-les bien, cela pourrait vous servir plus tard !"),
    TextBox("queen lily", "Puis, allez faire un gros bisou pour réveiller le PRINCE !")
], st.MAP_SURFACE)
RoomGaming = Room("Gaming Room", layout, st.MAP_SURFACE, enemies_number=0, pre_dialog=dialog, background_color=(58, 38, 58))