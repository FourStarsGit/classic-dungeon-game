import pygame
from src.main import settings as st
import asyncio

class IntroCinematic:
    def __init__(self):
        self.screen = st.SCREEN
        self.font = pygame.font.Font(st.FONT_PATH, 40)
        self.background = pygame.Surface((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        self.background.fill((0, 0, 0))
        self.text = "En l'an de grâce 1123..."
        self.fade_alpha = 0
        self.fade_speed = 2
        self.display_duration = 21000  # 21 seconds
        self.start_time = 0
        self.finished = False
        
    def start(self):
        self.start_time = pygame.time.get_ticks()
        st.LES_VISITEURS_SOUND.play(1)
        
    async def draw(self):
        self.screen.blit(self.background, (0, 0))
        
        # Render text with fade effect
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_surface.set_alpha(self.fade_alpha)
        text_rect = text_surface.get_rect(center=(st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2))
        self.screen.blit(text_surface, text_rect)

        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        
    async def update(self):
        current_time = pygame.time.get_ticks()
        time_passed = current_time - self.start_time
        
        # Handle fade in
        if time_passed < 2000:  # First 2 seconds
            self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
        # Handle fade out
        elif time_passed > self.display_duration - 2000:  # Last 2 seconds
            self.fade_alpha = max(0, self.fade_alpha - self.fade_speed)
            if self.fade_alpha <= 0:
                self.finished = True
        
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)
        

    def draw_screens(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))
        # Add semi-transparent overlay for better text readability
        self.screen.blit(self.overlay, (0, 0))
        
        current_intro = self.screens[self.current_screen]
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