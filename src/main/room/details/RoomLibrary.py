from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog
from src.main.room.Room import Room
from src.main.room.tile.Tile import *

# ROOM 1
layout = [
    [LibraryWall(), LibraryWall(), LibraryWall(), LibraryWall(), LibraryWall(), Door("UP"), Door("UP"), LibraryWall(), LibraryWall(), LibraryWall(), LibraryWall(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWall(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), WoodFloor(), LibraryWall()],
    [LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown(), LibraryWallDown()]
]
dialog = Dialog([
    TextBox("narrateur", "En ce beau matin de l'an 1123, la PRINCESSE réalisait une petite sieste."), 
    TextBox("narrateur", "Soudain, elle fut réveillée par sa fidèle acolyte, QUEEN LILY."),
    TextBox("queen lily", "PRINCESSE ! PRINCESSE ! Vite, réveillez-vous, c'est une catastrophe !!!"),
    TextBox("queen lily", "Le PRINCE a été enlevé !! Les méchants PAPIERS ADMINISTRATIFS l'ont capturé durant son court sommeil !"),
    TextBox("queen lily", "Vous devez absolument allez la sauver !! Elle saura vous récompenser comme il se doit !"),
    TextBox("queen lily", "Vous rappelez-vous comment sortir du lit, en vous délivrant de Morphée ?"),
    TextBox("queen lily", "Utilisez les flèches directionnelles ↑ ↓ ← → pour vous déplacer.")
], st.MAP_SURFACE)
RoomLibrary = Room("Bibliothèque", layout, st.MAP_SURFACE, enemies_number=0, pre_dialog=dialog, post_dialog=None)