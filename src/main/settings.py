import pygame

def resource_path(relative_path):
    return relative_path

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (233, 230, 21)
SNOW_COLOR = (245, 245, 248)

# WINDOW SETTINGS
GLOBAL_SCALE = 5
TILE_SIZE = 16 * GLOBAL_SCALE
TILES_W = 12
TILES_H = 9
SCREEN_WIDTH = TILE_SIZE * TILES_W
SCREEN_HEIGHT = TILE_SIZE * TILES_H

# Initialize this after pygame.init() is called
SCREEN = None

PLAYER_SPEED = 4

MAP_SURFACE = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WINDOW_TITLE = "Classic Dungeon Game"

# Initialize font after pygame.init() is called
pygame.font.init()
FONT_PATH = resource_path('assets/fonts/joystix monospace.otf')
FONT = pygame.font.Font(FONT_PATH, 20)
FONT_25 = pygame.font.Font(FONT_PATH, 25)

# Animation
FRAME_INDEX = 0
FRAME_SPEED = 10
SPRITE_WIDTH, SPRITE_HEIGHT = 60, 70  # Size of each sprite


# Dialog
DIALOG_WIDTH = SCREEN.get_width() - 40  # 20px padding on each side
DIALOG_SPEAKER_WIDTH = 150  # Fixed width for dialog speaker
DIALOG_HEIGHT = 150  # Fixed height for dialog box
DIALOG_X = 20
DIALOG_Y = SCREEN.get_height() - DIALOG_HEIGHT - 20  # 20px from bottom
SCRIPT_X = DIALOG_X + DIALOG_SPEAKER_WIDTH


# PATHS
SPRITE_PATH = resource_path("assets/sprites")
SPRITE_BACKGROUND_PATH = resource_path("assets/sprites/background")
IMG_BACKGROUND_PATH = resource_path("assets/backgrounds")
SOUND_PATH = resource_path("assets/sounds")
BLINDTEST_PATH = resource_path("assets/sounds/blindtest")

# DIALOG
DEFAULT_DIALOG_COLOR = (65, 48, 32)
HIGHLIGHTED_WORD_COLOR = (186, 40, 28)
HIGHLIGHTED_WORDS = ["PAPIERS", "ADMINISTRATIFS", "MAÏS", "DÉMONS", "PRINCE", "PRINCESSE", "QUEEN", "LILY", "CAPITAINE", "FRACASSE", "CLÉ", "DE", "DAME", "GINETTE", "TOUR", "KARIN", "MYSTÉRIEUSE", "BOITE.", "MYSTÉRIEUX", "PARCHEMIN.", "GROS", "SCARABÉE", "PYTHON", "LES", "COULOIRS", "DU", "TEMPS", "QUE", "TRÉPASSE", "SI", "JE", "FAIBLIS", "VIEUX"]

# SOUNDS
pygame.mixer.init()
PLAYER_ATTACK_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/player-attack.ogg")
PLAYER_ATTACK_SOUND.set_volume(0.5)
PLAYER_HIT_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/player-hit.ogg")
ENEMY_HIT_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/enemy-hit.ogg")
ENEMY_HIT_SOUND.set_volume(0.3)
ENEMY_KILL_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/explosion.ogg")
BOSS_ATTACK_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/boss-attack.ogg")
BOSS_ATTACK_SOUND.set_volume(0.3)
SPYRO_THE_DRAGON_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/spyro-the-dragon.ogg")
SPYRO_THE_DRAGON_SOUND.set_volume(0.2)
SPYRO_EPIC_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/spyro-twilight-harbor.ogg")
SPYRO_EPIC_SOUND.set_volume(0.3)
SUPER_NANAS_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/les-supers-nanas.ogg")
LES_VISITEURS_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/les-visiteurs-intro.ogg")
TIME_AFTER_TIME_SOUND = pygame.mixer.Sound(f"{SOUND_PATH}/time-after-time.ogg")
TIME_AFTER_TIME_SOUND.set_volume(0.2)
WINNING_BOSS = pygame.mixer.Sound(f"{SOUND_PATH}/winning-boss.ogg")
PLAYER_LOST = pygame.mixer.Sound(f"{SOUND_PATH}/player-lost.ogg")
CORRECT_ANSWER_SOUND = pygame.mixer.Sound(f'{SOUND_PATH}/correct.ogg')
WRONG_ANSWER_SOUND = pygame.mixer.Sound(f'{SOUND_PATH}/wrong.ogg')
MENU_MOVE_SOUND = pygame.mixer.Sound(f'{SOUND_PATH}/menu_move.ogg')
MENU_SELECT_SOUND = pygame.mixer.Sound(f'{SOUND_PATH}/menu_select.ogg')
MENU_BACK_SOUND = pygame.mixer.Sound(f'{SOUND_PATH}/type1.ogg')

# BLINDTEST
BACKGROUND_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/crash-brandicoot.ogg")
APPLAUSE_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/applause.ogg")
TOTALLY_SPIES_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/totally-spies.ogg")
KIM_POSSIBLE_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/kim-possible.ogg")
CODE_LYOKO_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/code-lyoko.ogg")
WINX_CLUB_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/winx-club.ogg")
GAME_OF_THRONES_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/game-of-thrones.ogg")
PLUS_BELLE_LA_VIE_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/plus-belle-la-vie.ogg")
KOH_LANTA_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/koh-lanta.ogg")
FULL_MONTY_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/full-monty.ogg")
INSPECTEUR_GADGET_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/inspecteur-gadget.ogg")
ASTERIX_ET_CLEOPATRE_SOUND = pygame.mixer.Sound(f"{BLINDTEST_PATH}/asterix-et-cleopatre.ogg")