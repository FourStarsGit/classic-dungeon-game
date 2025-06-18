from src.main.Boss import CaptainFracasse
from src.main.dialogs.TextBox import TextBox
from src.main.dialogs.Dialog import Dialog
from src.main.room.Room import Room
from src.main.room.tile.Tile import *

# ROOM 5
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

pre_dialog = Dialog([
    TextBox("queen lily", "Nous arrivons bientôt à la tour où est détenu le PRINCE !"),
    TextBox("queen lily", "Cependant, le CAPITAINE FRACASSE en garde l'entrée ! Vous devez le battre !"),
    TextBox("fracasse", "C'est moi qui ai la CLÉ DE DAME GINETTE qui ouvre l'entrée de la tour ! Mais tu ne l'auras jamais !"),
    TextBox("queen lily", "Pour vaincre le CAPITAINE FRACASSE : faites attention à sa couleur ! S'il est vert, alors il est vulnérable."),
    TextBox("queen lily", "S'il est rouge, fuyez pour ne pas perdre de points de vie (représentés par des coeurs en haut à gauche) !"),
    TextBox("queen lily", "La vie du CAPITAINE FRACASSE est représentée par des têtes de mort en bas à droite !")
], st.MAP_SURFACE)

post_dialog = Dialog([
    TextBox("fracasse", "Raaaaaaahhhhhhhhhhhhhhhhhhhhhhhh..."),
    TextBox("queen lily", "Félicitations !!! Vous avez éclaté le méchant CAPITAINE FRACASSE !"),
    TextBox("queen lily", "En mourant dans d'atroces souffrances, il laisse tomber la CLÉ DE DAME GINETTE permettant d'ouvrir la prochaine porte !"),
    TextBox("queen lily", "Votre santé est restaurée et vous gagnez un coeur supplémentaire.")
], st.MAP_SURFACE)

RoomPathEnd = Room("Le capitaine", 
    layout, 
    st.MAP_SURFACE, 
    background_color=st.SNOW_COLOR, 
    pre_dialog=pre_dialog, 
    post_dialog=post_dialog,
    boss=CaptainFracasse(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2, st.SCREEN),
    music=st.SPYRO_EPIC_SOUND)