import pygame
from src.main import settings as st

ICON = pygame.image.load(f"{st.SPRITE_PATH}/icon.png").convert_alpha()

PLAYER_SHEET = pygame.image.load(f"{st.SPRITE_PATH}/player/walk.png").convert_alpha()
PLAYER_ATTACK_SHEET = pygame.image.load(f"{st.SPRITE_PATH}/player/attack.png").convert_alpha()
HEART_IMAGE = pygame.image.load(f"{st.SPRITE_PATH}/heart.png").convert_alpha()
HEART_IMAGE = pygame.transform.smoothscale(HEART_IMAGE, (30, 30))
DEAD_HEAD_IMAGE = pygame.image.load(f"{st.SPRITE_PATH}/dead-head.png").convert_alpha()
DEAD_HEAD_IMAGE = pygame.transform.smoothscale(DEAD_HEAD_IMAGE, (30, 30))

SCRIPT = pygame.image.load(f'{st.SPRITE_PATH}/script.png').convert()

ENEMY_MAIZE = pygame.image.load(f"{st.SPRITE_PATH}/enemies/maize.png").convert_alpha()
ENEMY_MAIZE = pygame.transform.smoothscale(ENEMY_MAIZE, (50, 70))
ENEMY_DEMON = [pygame.transform.smoothscale(
    pygame.image.load(f"{st.SPRITE_PATH}/enemies/demon/frame{x}.png").convert_alpha(),
    (st.TILE_SIZE, st.TILE_SIZE)) for x in range(1, 5)]
ENEMY_PAPER = pygame.image.load(f"{st.SPRITE_PATH}/enemies/paper.png").convert_alpha()
ENEMY_PAPER = pygame.transform.smoothscale(ENEMY_PAPER, (st.TILE_SIZE, st.TILE_SIZE))

ENEMY_EXPLOSION = [pygame.transform.smoothscale(
    pygame.image.load(f"{st.SPRITE_PATH}/enemies/explosion/frame{x}.png").convert_alpha(), 
    (st.TILE_SIZE, st.TILE_SIZE)) for x in range(1, 7)]

CAPTAIN_FRACASSE = pygame.image.load(f"{st.SPRITE_PATH}/enemies/captain_fracasse.png").convert_alpha()
CAPTAIN_FRACASSE = pygame.transform.smoothscale(CAPTAIN_FRACASSE, (st.TILE_SIZE * 1.5, st.TILE_SIZE * 1.5))
BEETLE = pygame.image.load(f"{st.SPRITE_PATH}/enemies/beetle.png").convert_alpha()
BEETLE = pygame.transform.smoothscale(BEETLE, (st.TILE_SIZE * 1.5, st.TILE_SIZE * 1.5))
PYTHON = pygame.image.load(f"{st.SPRITE_PATH}/enemies/python.png").convert_alpha()
PYTHON = pygame.transform.smoothscale(PYTHON, (st.TILE_SIZE * 1.1, st.TILE_SIZE * 1.1))
OLD_DEMON = pygame.image.load(f"{st.SPRITE_PATH}/enemies/old_demon.png").convert_alpha()
OLD_DEMON = pygame.transform.smoothscale(OLD_DEMON, (st.TILE_SIZE * 1.2, st.TILE_SIZE * 1.2))

VALIDATE_SIGN = pygame.image.load(f'{st.SPRITE_PATH}/validate.png').convert_alpha()
VALIDATE_SIGN = pygame.transform.scale(VALIDATE_SIGN, (50, 50))
ERROR_SIGN = pygame.image.load(f'{st.SPRITE_PATH}/error.png').convert_alpha()
ERROR_SIGN = pygame.transform.scale(ERROR_SIGN, (50, 50))
