import pygame
from src.main import settings as st
import asyncio

class GameOverMenu:
    def __init__(self):
        self.screen = st.SCREEN
        self.font_large = pygame.font.Font(st.FONT_PATH, 54)
        self.font_medium = pygame.font.Font(st.FONT_PATH, 40)
        self.font_small = pygame.font.Font(st.FONT_PATH, 25)
        self.selected_option = 0
        self.options = ["Réessayer", "Quitter"]
        
        # Load and scale background image
        self.background = pygame.image.load(f'{st.IMG_BACKGROUND_PATH}/background.png').convert()
        self.background = pygame.transform.scale(self.background, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        
        self.fade_alpha = 255
        self.fade_speed = 5
        # Add semi-transparent overlay for better text readability
        self.overlay = pygame.Surface((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        self.overlay.fill((0, 0, 0))
        self.overlay.set_alpha(128)  # 50% transparency
        self.background_color = (0, 0, 0)  # Black background
        self.text_color = (255, 255, 255)  # White text
        self.selected_color = (255, 215, 0)  # Gold color for selected option
        self.disabled_color = (128, 128, 128)  # Gray color for disabled options

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

    def draw_menu(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))
        # Add semi-transparent overlay for better text readability
        self.screen.blit(self.overlay, (0, 0))
        
        # Draw title with fade effect
        title = "Tu as perdu.\nAlors, ils sont où tes réflexes ?"
        self.draw_text_centered(title, self.font_small, self.text_color, -100, int(self.fade_alpha))

        # Draw options
        for i, option in enumerate(self.options):
            color = self.selected_color if i == self.selected_option else self.text_color
            alpha = max(0, min(255, int(self.fade_alpha - 50)))  # Options appear slightly after title
            self.draw_text_centered(option, self.font_medium, color, 50 + i * 60, alpha)

    def update(self, events):
        # Handle menu 
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.options[self.selected_option]
        
        # Fade in menu
        if self.fade_alpha < 255:
            self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
            
        return None

    async def draw(self):
        self.draw_menu()
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)