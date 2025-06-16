from src.main.menu.EndingMenu import EndingMenu
from src.main.room.room_layout import rooms
from src.main.BlindtestTreasure import BlindtestTreasure
from src.main.TitleGame import TitleGame
from src.main import settings as st
import pygame
from src.main.Player import Player
from src.main.room.room_layout import *
import src.main.sprites as sprites
import asyncio


# Singleton pattern
class GameMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=GameMeta):
    def __init__(self, save_manager):
        self.save_manager = save_manager
        self.play_blindtest = False
        self.play_title_game = False
        self.play_ending_menu = False
        self.game_end = False
        self.blindtest = BlindtestTreasure()
        self.title_game = TitleGame()
        self.ending_menu = EndingMenu()
        self.starting_room = RoomLibrary
        self.current_room = self.starting_room
        self.running_game = True
        self.player_is_dead = False

    async def check_door_transition(self, current_room, player, save_data):
        rooms_with_index = list(rooms)
        idx = rooms_with_index.index(current_room)

        if player.rect.y < 0 or player.rect.y > st.SCREEN_HEIGHT:
            # Create a transition effect when changing rooms
            transition_surface = pygame.Surface((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
            transition_surface.fill(st.BLACK)
            
            for alpha in range(0, 255, 15):  # Fade out
                transition_surface.set_alpha(alpha)
                st.SCREEN.blit(transition_surface, (0,0))
                pygame.display.flip()
                pygame.time.delay(30)
                await asyncio.sleep(0)

            if player.rect.y < 0:
                new_room_index = idx + 1
                player.pos.y = st.SCREEN_HEIGHT - st.TILE_SIZE
            else:
                new_room_index = idx - 1
                player.pos.y = st.TILE_SIZE

            self.current_room = rooms_with_index[new_room_index]
            player.pos.x = st.SCREEN_WIDTH // 2
            player.rect.center = player.pos
            self.current_room.draw(save_data["enemies_defeated"][str(rooms.index(self.current_room))])
    
    async def start(self, running, continue_game):
        # Load game state
        self.running_game = True
        save_data = self.save_manager.load_game()
        if continue_game:
            current_room = rooms[save_data["current_room_index"]]
            # Load player position
            player = Player(st.SCREEN)
            hearts = current_room.boss.give_hearts - 1 if current_room.has_boss else save_data["hearts"]
            player.current_hearts = hearts
            # Load room states
            if save_data["room_states"].get(str(save_data["current_room_index"])):
                current_room.door_open = save_data["room_states"][str(save_data["current_room_index"])]
            # Set number of enemies based on saved data
            if str(save_data["current_room_index"]) in save_data["enemies_defeated"]:
                remaining = save_data["enemies_defeated"][str(save_data["current_room_index"])]
                if remaining < len(current_room.enemies):
                    current_room.enemies = current_room.enemies[:remaining]
                current_room.enemies_number = len(current_room.enemies)
        else:
            current_room = self.starting_room
            current_room.music.play(-1)
            player = Player(st.SCREEN)
            # Initialize enemies_remaining for a new game
            save_data["enemies_defeated"] = {}
            for i, room in enumerate(rooms):
                save_data["enemies_defeated"][str(i)] = len(room.enemies)
        
        # Add attacking state variables
        player.attacking = False
        self.player_is_dead = False
        player.attack_timer = 0
        ATTACK_DURATION = 200  # Attack animation lasts 500ms
        end_game_start_time = 0
        player_movement = True
        
        current_room.draw(save_data["enemies_defeated"][str(rooms.index(current_room))])
        
        # Game loop
        clock = pygame.time.Clock()
        
        while running:
            st.SCREEN.fill(st.WHITE)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Save game before quitting
                    save_data = {
                        "current_room_index": rooms.index(current_room),
                        "hearts": player.current_hearts,
                        "enemies_defeated": save_data["enemies_defeated"],
                        "room_states": save_data["room_states"]
                    }
                    self.save_manager.save_game(save_data)
                    running = False
                    self.running_game = False
                    pygame.quit()
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and current_room.pre_dialog_shown:
                        player.attacking = True
                        player.attack_timer = pygame.time.get_ticks()
                        st.PLAYER_ATTACK_SOUND.play()
                    if event.key == pygame.K_RETURN and current_room.pre_dialog and (current_room.post_dialog_shown ^ (current_room.boss is not None)):
                        current_room.update()
                        if not current_room.pre_dialog.textbox_currently_typing:
                            current_room.pre_dialog.next_line()
                            if current_room.pre_dialog.current_line >= len(current_room.pre_dialog.textboxes):
                                current_room.pre_dialog_shown = True
                                current_room.pre_dialog = None
                                current_room.draw(save_data["enemies_defeated"][str(rooms.index(current_room))])
                    if event.key == pygame.K_RETURN and current_room.post_dialog and current_room.boss is None:
                        current_room.update()
                        if not current_room.post_dialog.textbox_currently_typing:
                            current_room.post_dialog.next_line()
                            if current_room.post_dialog.current_line >= len(current_room.post_dialog.textboxes):
                                current_room.post_dialog_shown = True
                                current_room.post_dialog = None
                                current_room.draw(save_data["enemies_defeated"][str(rooms.index(current_room))])
            
            # Draw static map
            st.SCREEN.blit(st.MAP_SURFACE, (0, 0))
            
            # Movement
            if player_movement:
                player.key_press(pygame.key.get_pressed(), current_room)
                
                player.rect.centerx = int(player.pos.x)
                player.collide_with_walls(current_room.walls, 'x')
                player.rect.centery = int(player.pos.y)
                player.collide_with_walls(current_room.walls, 'y')
                player.rect.center = (int(player.pos.x), int(player.pos.y))
                player.pos += player.vel
            
            # Save previous room to check if room changed
            previous_room = current_room
            await self.check_door_transition(current_room, player, save_data)
            current_room = self.current_room
            
            # If room changed, save the game
            if previous_room != current_room:
                previous_room.music.stop()
                current_room.music.play(-1)
                save_data["room_states"][str(rooms.index(previous_room))] = previous_room.door_open
                
                save_data.update({
                    "current_room_index": rooms.index(current_room),
                    "hearts": player.current_hearts,
                })
                self.save_manager.save_game(save_data)
                
            # Update and draw enemies
            for enemy in current_room.enemies:
                enemy.update(player.pos, current_room.walls)
                if enemy.collide_with_player(player):
                    pass
                enemy.spawn()
                
            if current_room.pre_dialog_shown:
                player.spawn()
            
            # Display life bar
            for i in range(player.current_hearts):
                st.SCREEN.blit(sprites.HEART_IMAGE, (10 + i * 35, 10))

            if current_room.has_boss and current_room.pre_dialog_shown:
                boss_health_rect = pygame.Surface((current_room.boss.health * 35 + 5, 40))
                boss_health_rect.fill(st.BLACK)
                st.SCREEN.blit(boss_health_rect, (st.SCREEN_WIDTH - 305, st.SCREEN_HEIGHT - 45))
                for i in range(current_room.boss.health):
                    st.SCREEN.blit(sprites.DEAD_HEAD_IMAGE, (st.SCREEN_WIDTH - 300 + i * 35, st.SCREEN_HEIGHT - 40))
                
            # Display room name
            room_text = st.FONT.render(current_room.room_name, True, st.WHITE)
            text_width, text_height = room_text.get_size()
            room_name_rect = pygame.Surface((text_width + 20, text_height + 10))  # Add padding
            room_name_rect.fill(st.BLACK)
            room_name_rect.set_alpha(150)
            st.SCREEN.blit(room_name_rect, (700, 10))
            st.SCREEN.blit(room_text, (710, 15))
            
            # Update attack state and handle enemy collisions
            # In the game loop where you handle player attacks
            if player.attacking:
                # Check collision with BlindtestTreasure tiles
                if not current_room.blindtest_treasure_complete and not self.play_blindtest:
                    for tile, x, y in current_room.get_treasure_tiles():
                        # Create a larger collision rect that extends in all directions
                        tile_rect = pygame.Rect((x + 0.9) * st.TILE_SIZE, (y - 1.1) * st.TILE_SIZE, st.TILE_SIZE * 1.2, st.TILE_SIZE * 1.2 )
                        if isinstance(tile, BlindtestTreasureTile) and (player.rect.colliderect(tile_rect)):
                            self.play_blindtest = True
                            player_movement = False
                            current_room.music.stop()
                            self.blindtest.start_blindtest()

                if not current_room.title_game_complete and not self.play_title_game:
                    for tile, x, y in current_room.get_title_game_tiles():
                        # Create a larger collision rect that extends in all directions
                        tile_rect = pygame.Rect((x + 0.9) * st.TILE_SIZE, (y - 1.1) * st.TILE_SIZE, st.TILE_SIZE * 1.2, st.TILE_SIZE * 1.2)
                        if isinstance(tile, TitleGameTile) and (player.rect.colliderect(tile_rect)):
                            self.play_title_game = True
                            player_movement = False
                            self.title_game.start()

                if current_room is RoomGaming:
                    for tile, x, y in current_room.get_sleeping_man_tiles():
                        # Create a larger collision rect that extends in all directions
                        tile_rect = pygame.Rect((x + 0.9) * st.TILE_SIZE, (y - 1.1) * st.TILE_SIZE, st.TILE_SIZE * 1.2, st.TILE_SIZE * 1.2)
                        if isinstance(tile, SleepingManTile) and (player.rect.colliderect(tile_rect)):
                            self.play_ending_menu = True
                            current_room.music.stop()
                            player_movement = False
                            self.ending_menu.draw_intro_screen()

                current_time = pygame.time.get_ticks()
                if current_time - player.attack_timer > ATTACK_DURATION:
                    player.attacking = False
                    player.spawn()
                else:
                    # Calculate attack frame based on attack timer
                    attack_progress = (pygame.time.get_ticks() - player.attack_timer) / ATTACK_DURATION
                    attack_frame = int(attack_progress * len(player.frames_attack))
                    attack_frame = min(attack_frame, len(player.frames_attack) - 1)
                    
                    # Get the correct attack sprite based on player direction
                    attack_sprite = player.frames_attack[attack_frame]
                    if player.facing_left:
                        attack_sprite = pygame.transform.flip(attack_sprite, True, False)
                    
                    # Position the attack sprite relative to player
                    attack_pos = (player.rect.centerx - attack_sprite.get_width()//2,
                                player.rect.centery - attack_sprite.get_height()//2)
                    st.SCREEN.blit(attack_sprite, attack_pos)
                    
                    for enemy in list(current_room.enemies):
                        if player.rect.colliderect(enemy.rect):
                            if enemy.hit():
                                current_room.enemies.remove(enemy)
                                current_room.enemies_number -= 1
                                # Display explosion animation when enemy is defeated
                                explosion_pos = (enemy.rect.x, enemy.rect.y)
                                st.ENEMY_KILL_SOUND.play()
                                
                                # Create an explosion animation object that will update independently
                                explosion_start_time = pygame.time.get_ticks()
                                current_room.active_explosions.append({
                                    'position': explosion_pos,
                                    'start_time': explosion_start_time,
                                    'frame': 0
                                })
                                
                                # Update enemies_remaining in save data
                                room_idx = str(rooms.index(current_room))
                                save_data["enemies_defeated"][room_idx] += 1
                                self.save_manager.save_game(save_data)
            
            if self.play_blindtest:
                self.blindtest.draw_blindtest(st.SCREEN)
                self.play_blindtest = self.blindtest.handle_input(event)
                if not self.play_blindtest:
                    current_room.music.play(-1)
                    current_room.draw(save_data["enemies_defeated"][str(rooms.index(current_room))])
                    current_room.blindtest_treasure_complete = True
                    end_game_start_time = pygame.time.get_ticks()


            if self.play_title_game:
                self.title_game.draw()
                self.play_title_game = self.title_game.handle_input(event)
                if not self.play_title_game:
                    current_room.draw(save_data["enemies_defeated"][str(rooms.index(current_room))])
                    current_room.title_game_complete = True
            
            if current_room.blindtest_treasure_complete and pygame.time.get_ticks() - end_game_start_time < 8000 and current_room.has_blindtest_treasure:
                script = pygame.transform.scale(sprites.SCRIPT, (st.DIALOG_WIDTH, 180))
                script_rect = pygame.Rect(st.DIALOG_X, st.SCREEN_HEIGHT // 2, st.DIALOG_WIDTH, 300)
                st.SCREEN.blit(script, script_rect)
                menu_rect = pygame.Rect(st.DIALOG_X, st.SCREEN_HEIGHT // 2, st.DIALOG_WIDTH, 300)
                pygame.draw.rect(st.SCREEN, st.DEFAULT_DIALOG_COLOR, menu_rect, 2)
                menu_text_1 = st.FONT_25.render("Tu as terminé le blindtest !!!", True, st.DEFAULT_DIALOG_COLOR)
                menu_text_2 = st.FONT_25.render("Résultat :", True, st.DEFAULT_DIALOG_COLOR)
                menu_text_3 = st.FONT_25.render(f"{self.blindtest.score}/50", True, st.BLACK)
                menu_text_4 = st.FONT_25.render("Bravo ! Tu peux avancer...", True, st.DEFAULT_DIALOG_COLOR)
                line_height = st.FONT_25.get_linesize()
                st.SCREEN.blit(menu_text_1, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 + line_height))
                st.SCREEN.blit(menu_text_2, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 2)))
                st.SCREEN.blit(menu_text_3, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 3)))
                st.SCREEN.blit(menu_text_4, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 4)))
                player_movement = False
            elif current_room.blindtest_treasure_complete and pygame.time.get_ticks() - end_game_start_time >= 8000 and not self.title_game.is_active:
                player_movement = True
            elif self.title_game.is_active:
                player_movement = False
            current_room.check_door_status(save_data["enemies_defeated"][str(rooms.index(current_room))])
            current_room.update()

            if self.play_ending_menu:
                self.ending_menu.draw_intro_screen()
                self.play_ending_menu = self.ending_menu.update(event)
                if not self.play_ending_menu:
                    self.game_end = True
                    self.running_game = False
                    #return False
                    break
            
            # Draw save indicator
            self.save_manager.draw_save_indicator(st.SCREEN)
                        
            # Update player invulnerability
            current_time = pygame.time.get_ticks()
            if player.invulnerable:
                if current_time - player.invulnerable_timer > player.invulnerable_duration:
                    player.invulnerable = False
                    player.invulnerable_timer = 0
                    

            # Update and handle boss
            if current_room.has_boss and current_room.boss and current_room.pre_dialog_shown:
                current_room.boss.update(player.pos, current_room.walls)
                current_room.boss.spawn()
                
                if player.attacking:
                    if current_room.boss.rect.colliderect(player.rect):
                        if current_room.boss.hit():
                            if current_room.boss.health <= 0:
                                player.current_hearts = current_room.boss.give_hearts
                                current_room.boss = None
                                current_room.has_boss = False
                                st.WINNING_BOSS.play()
                                save_data["enemies_defeated"][str(rooms.index(current_room))] += 1
                                self.save_manager.save_game(save_data)
                
                if current_room.boss is not None and current_room.boss.collide_with_player(player) and \
                    not current_room.boss.is_vulnerable and not current_room.boss.being_hit:
                    if player.hit(current_room.boss.pos):
                        st.PLAYER_HIT_SOUND.play()
                        if player.current_hearts <= 0:
                            st.PLAYER_LOST.play()
                            self.player_is_dead = True
                            await asyncio.sleep(0)
                            break

            # Handle active explosions
            current_time = pygame.time.get_ticks()
            for explosion in list(current_room.active_explosions):
                time_elapsed = current_time - explosion['start_time']
                if time_elapsed >= 11:  # Update every ~33ms (30 FPS)
                    explosion['frame'] += 1
                    explosion['start_time'] = current_time
                    # Calculate which frame of the explosion animation to show
                    frame_index = min(explosion['frame'] // 4, len(sprites.ENEMY_EXPLOSION) - 1)
                    if frame_index >= len(sprites.ENEMY_EXPLOSION) - 1:  # Remove after last frame is shown
                        st.SCREEN.blit(sprites.ENEMY_EXPLOSION[-1], explosion['position'])  # Show final frame
                        current_room.active_explosions.remove(explosion)  # Then remove explosion
                    else:
                        # Display the current frame of the explosion animation
                        st.SCREEN.blit(sprites.ENEMY_EXPLOSION[frame_index], explosion['position'])

            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)
        self.running_game = False
        return False

    def stop(self):
        st.SCREEN.fill(st.BLACK)
    
    async def end_screen(self):
        st.SCREEN.fill(st.BLACK)
        text_surface = st.FONT.render("THE END, tu peux fermer ou rafraichir la fenêtre :)", True, st.WHITE)
        text_rect = text_surface.get_rect(center=(st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2))
        st.SCREEN.blit(text_surface, text_rect)
        st.TIME_AFTER_TIME_SOUND.stop()
        self.current_room.music.stop()
        self.running_game = False
        self.game_end = True
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
