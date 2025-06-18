import pygame
import asyncio
from src.main import settings as st
from src.main.SaveManager import SaveManager

class Menu:
    def __init__(self):
        self.screen = st.SCREEN
        self.font_large = pygame.font.Font(st.FONT_PATH, 54)
        self.font_medium = pygame.font.Font(st.FONT_PATH, 40)
        self.font_small = pygame.font.Font(st.FONT_PATH, 25)
        self.selected_option = 0
        self.options = ["Commencer", "Continuer"]
        
        # Initialize save manager
        self.save_manager = SaveManager()
        
        # Load and scale background image
        self.background = pygame.image.load(f'{st.IMG_BACKGROUND_PATH}/background.png').convert()
        self.background = pygame.transform.scale(self.background, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        
        # Load sound effects
        self.type_sounds = [
            pygame.mixer.Sound(f'{st.SOUND_PATH}/type1.ogg'),
            pygame.mixer.Sound(f'{st.SOUND_PATH}/type2.ogg'),
            pygame.mixer.Sound(f'{st.SOUND_PATH}/type3.ogg'),
            pygame.mixer.Sound(f'{st.SOUND_PATH}/type4.ogg')
        ]
        # Set lower volume for typing sounds
        for sound in self.type_sounds:
            sound.set_volume(0.3)
        
        # Add semi-transparent overlay for better text readability
        self.overlay = pygame.Surface((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        self.overlay.fill((0, 0, 0))
        self.overlay.set_alpha(128)  # 50% transparency
        
        self.intro_screens = [
            {"text": "Bienvenue", "duration": 3000, "font": self.font_large},
            {"text": "Ce jeu vidéo a été\nspécialement créé pour toi...", "duration": 5000, "font": self.font_medium},
            {"text": "...afin de te souhaiter un \n<<TEXTE PERSONNALISÉ>>", "duration": 5000, "font": self.font_medium},
        ]
        self.current_screen = 0
        self.screen_timer = 0
        self.background_color = (0, 0, 0)  # Black background
        self.text_color = (255, 255, 255)  # White text
        self.selected_color = (255, 215, 0)  # Gold color for selected option
        self.disabled_color = (128, 128, 128)  # Gray color for disabled options
        
        # Animation properties
        self.char_index = 0
        self.char_timer = 0
        self.char_delay = 50  # Milliseconds between each character
        self.fade_alpha = 0
        self.fade_speed = 5
        self.animation_complete = False
        self.current_text = ""
        
        # Sound properties
        self.last_sound_index = 0
        self.sound_variation_counter = 0
        self.sound_variation_threshold = 2  # Play sound every N characters
        self.music_is_playing = False

    def play_type_sound(self):
        # Rotate through available sounds
        self.sound_variation_counter += 1
        if self.sound_variation_counter >= self.sound_variation_threshold:
            self.sound_variation_counter = 0
            self.last_sound_index = (self.last_sound_index + 1) % len(self.type_sounds)
            self.type_sounds[self.last_sound_index].play()

    def draw_text_centered(self, text, font, color, y_offset=0, alpha=255):
        # Handle multiline text
        lines = text.split('\n')
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            # Create a new surface with per-pixel alpha
            alpha_surface = pygame.Surface(text_surface.get_rect().size, pygame.SRCALPHA)
            # Ensure alpha is an integer between 0 and 255
            alpha = max(0, min(255, int(alpha)))
            # Set the alpha of the entire surface
            alpha_surface.fill((255, 255, 255, alpha))
            # Blit with alpha
            text_surface.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            text_rect = text_surface.get_rect(center=(st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2 + y_offset + i*50))
            self.screen.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.time.Clock().tick(60)

    def draw_intro_screen(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))
        # Add semi-transparent overlay for better text readability
        self.screen.blit(self.overlay, (0, 0))
        
        current_intro = self.intro_screens[self.current_screen]
        full_text = current_intro["text"]
        
        # If animation is not complete, show partial text with typewriter effect
        if not self.animation_complete:
            # Update current text based on char_index
            if self.char_index < len(full_text):
                self.current_text = full_text[:self.char_index + 1]
            
            # Fade in effect
            if self.fade_alpha < 255:
                self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
            
            self.draw_text_centered(self.current_text, current_intro["font"], self.text_color, 0, self.fade_alpha)
        else:
            # Show complete text
            self.draw_text_centered(full_text, current_intro["font"], self.text_color)
        pygame.display.flip()

    def draw_menu(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))
        # Add semi-transparent overlay for better text readability
        self.screen.blit(self.overlay, (0, 0))
        
        # Play menu music in loop if not already playing
        if not self.music_is_playing:
            self.music_is_playing = True
            st.SUPER_NANAS_SOUND.play(-1)  # -1 means loop indefinitely
        
        # Draw title with fade effect
        self.draw_text_centered(st.WINDOW_TITLE, self.font_medium, self.text_color, -100, int(self.fade_alpha))

        # Draw options
        for i, option in enumerate(self.options):
            # Determine color based on whether Continue is available
            if option == "Continuer" and not self.save_manager.has_save():
                color = self.disabled_color
            else:
                color = self.selected_color if i == self.selected_option else self.text_color
            alpha = max(0, min(255, int(self.fade_alpha - 50)))  # Options appear slightly after title
            self.draw_text_centered(option, self.font_medium, color, 50 + i * 60, alpha)

    def update(self, events):
        current_time = pygame.time.get_ticks()
        
        # Handle intro screens
        if self.current_screen < len(self.intro_screens):
            # Initialize timers if needed
            if self.screen_timer == 0:
                self.screen_timer = current_time
                self.char_timer = current_time
                self.char_index = 0
                self.fade_alpha = 0
                self.animation_complete = False
                self.current_text = ""
                self.sound_variation_counter = 0
            
            # Update typewriter effect
            if not self.animation_complete:
                if current_time - self.char_timer >= self.char_delay:
                    if self.char_index < len(self.intro_screens[self.current_screen]["text"]):
                        old_index = self.char_index
                        self.char_index += 1
                        self.char_timer = current_time
                        # Only play sound for actual characters (not spaces or newlines)
                        if self.intro_screens[self.current_screen]["text"][old_index] not in [' ', '\n']:
                            self.play_type_sound()
                    else:
                        self.animation_complete = True
            
            # Check if it's time to move to next screen
            if current_time - self.screen_timer >= self.intro_screens[self.current_screen]["duration"] and self.animation_complete:
                if self.current_screen < len(self.intro_screens) - 1:
                    self.current_screen += 1
                    self.screen_timer = current_time
                    self.char_index = 0
                    self.fade_alpha = 0
                    self.animation_complete = False
                    self.current_text = ""
                    self.sound_variation_counter = 0
                else:
                    self.current_screen = len(self.intro_screens)  # Move to menu
                    self.fade_alpha = 0
            return None

        # Handle menu input
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    selected = self.options[self.selected_option]
                    if selected == "Continuer" and not self.save_manager.has_save():
                        return None  # Don't allow Continue if no save exists
                    st.SUPER_NANAS_SOUND.stop()
                    return selected
        
        # Fade in menu
        if self.fade_alpha < 255:
            self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
            
        return None

    async def draw(self):
        if self.current_screen < len(self.intro_screens):
            self.draw_intro_screen()
        else:
            self.draw_menu()
        
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)