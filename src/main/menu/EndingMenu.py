import pygame
from src.main import settings as st

class EndingMenu:
    def __init__(self):
        self.screen = st.SCREEN
        self.font_large = pygame.font.Font(st.FONT_PATH, 54)
        self.font_medium = pygame.font.Font(st.FONT_PATH, 40)
        self.font_small = pygame.font.Font(st.FONT_PATH, 25)
        self.selected_option = 0
        self.options = ["Commencer", "Continuer"]
        self.padding_x = 30
        self.padding_y = 20
        
        # Load and scale background image
        self.background = pygame.image.load(f'{st.IMG_BACKGROUND_PATH}/love-background.jpg').convert()
        self.background = pygame.transform.scale(self.background, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        
        # Add semi-transparent overlay for better text readability
        self.overlay = pygame.Surface((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        self.overlay.fill((0, 0, 0))
        self.overlay.set_alpha(128)  # 50% transparency
        
        self.intro_screens = [
            {"text": "Félicitations !", "font": self.font_large},
            {"text": "Tu as intégralement\nterminé le jeu !", "font": self.font_medium},
            {"text": "Tu gagnes : .................", "font": self.font_medium},
            {"text": "<<TEXTE PERSONNALISÉ>>", "font": self.font_medium},
            {"text": "<3", "font": self.font_medium}
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

    def draw_intro_screen(self):

        if not pygame.mixer.get_busy():
            st.TIME_AFTER_TIME_SOUND.play(-1)

        if self.current_screen >= len(self.intro_screens):
            return False

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

    def update(self, event):
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
                    else:
                        self.animation_complete = True

            if self.animation_complete:
                prompt_image = pygame.image.load(f'{st.SPRITE_PATH}/enter.png').convert_alpha()
                prompt_image = pygame.transform.scale(prompt_image, (30, 30))
                prompt_rect = pygame.Rect(st.DIALOG_X + st.DIALOG_WIDTH - self.padding_x - 30, 
                                        st.DIALOG_Y + st.DIALOG_HEIGHT - self.padding_y - 30, 30, 30)
                st.SCREEN.blit(prompt_image, prompt_rect)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.animation_complete:
                    if self.current_screen < len(self.intro_screens):
                        self.current_screen += 1
                        self.screen_timer = current_time
                        self.char_index = 0
                        self.fade_alpha = 0
                        self.animation_complete = False
                        self.current_text = ""
                        self.sound_variation_counter = 0

            return True

        return False
