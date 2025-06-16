#!/usr/bin/env python3

# /// script
# dependencies = [
#     "pygame-ce"
# ]
# 
# modules = [
#     "src"
# ]
# ///

import pygame
import asyncio
from src.main.menu.Menu import Menu
from src.main import settings as st
from src.main import sprites
from src.main.menu.GameOverMenu import GameOverMenu
from src.main.SaveManager import SaveManager
from src.main.Game import Game
from src.main.menu.Cinematic import IntroCinematic
import hashlib

async def main():
    quit_menu = False
    running_game = False
    clock = pygame.time.Clock()
    running = True
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption(st.WINDOW_TITLE)
    pygame.display.set_icon(sprites.ICON)

    save_manager = SaveManager()
    menu = Menu()
    game = Game(save_manager)
    game_over_menu = GameOverMenu()
    intro_cinematic = IntroCinematic()

    while running:

        if not pygame.get_init():
            return False

        # Handle password check before game starts
        if not hasattr(game, 'password_verified'):
            # Create a simple password input surface
            password_surface = pygame.Surface((400, 100))
            password_surface.fill((50, 50, 50))
            background = pygame.image.load(f'{st.IMG_BACKGROUND_PATH}/background.png').convert()
            background = pygame.transform.scale(background, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
            password_input = ""
            password_hash = "72e1a34ee07b8485aeff9bfc8ce38502df03ec8647ab38bdd3b3cf4c4c3f36f7" # SHA256 for "thomaszuk"
            
            while not hasattr(game, 'password_verified'):
                password_surface.fill((50, 50, 50))
                events = pygame.event.get()
                
                for event in events:
                    if event.type == pygame.QUIT:
                        running = False
                        return False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pygame.event.clear()
                            # Verify password using SHA-256
                            hashed_input = hashlib.sha256(password_input.encode()).hexdigest()
                            if hashed_input == password_hash:
                                game.password_verified = True
                            else:
                                password_input = ""
                        elif event.key == pygame.K_BACKSPACE:
                            password_input = password_input[:-1]
                        else:
                            if len(password_input) < 20:  # Limit password length
                                password_input += event.unicode
                
                # Draw password prompt
                text = st.FONT_25.render("Mot de pass : " + "*" * len(password_input), True, (255, 255, 255))
                text_rect = text.get_rect(center=(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2))
                st.SCREEN.blit(background, (0, 0))
                st.SCREEN.blit(text, text_rect)
                pygame.display.flip()
                clock.tick(60)
                await asyncio.sleep(0)

        events = pygame.event.get()
        # Handle game over menu
        if not running_game and quit_menu is True and game.player_is_dead:
            game.stop()
            await game_over_menu.draw()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    return False
            selected_option_restart = game_over_menu.update(events)
            if selected_option_restart == "Quitter":
                running_game = False
                await game.end_screen()
                break
            elif selected_option_restart == "Réessayer":
                await game.start(running, continue_game=True)
                running_game = game.running_game
                quit_menu = True
            
            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)
            continue

        for event in events:
            if event.type == pygame.QUIT:
                running = False
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and menu.current_screen < len(menu.intro_screens):  # Press 'Enter' to bypass intro and start new game
                    menu.current_screen = len(menu.intro_screens)  # Skip intro screens
                    pygame.event.clear()  # Clear all events
                    events = pygame.event.get()
                    break

        if not quit_menu:
            await menu.draw()
            selected_option = menu.update(events)
            if selected_option == "Commencer":
                # Show intro cinematic before starting the game
                intro_cinematic.start()
                while not intro_cinematic.finished:
                    await intro_cinematic.draw()
                    await intro_cinematic.update()
                    pygame.display.flip()
                    clock.tick(60)
                    await asyncio.sleep(0)
                    # Allow skipping the cinematic
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                            intro_cinematic.finished = True
                            st.LES_VISITEURS_SOUND.stop()
                            break
                
                st.LES_VISITEURS_SOUND.stop()
                await game.start(running, continue_game=False)
                running_game = game.running_game
                quit_menu = True
    
            elif selected_option == "Continuer":
                await game.start(running, continue_game=True)
                running_game = game.running_game
                quit_menu = True

        
        if game.game_end or (running_game is False and intro_cinematic.finished):
            await game.end_screen()
        
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    clock.tick(60)
    await asyncio.sleep(0)

# Run the game
asyncio.run(main())
