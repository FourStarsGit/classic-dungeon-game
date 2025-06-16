import pygame

from src.main import settings as st, sprites

class Dialog:
    def __init__(self, textboxes, screen):
        self.color = (255, 255, 255)
        self.position = (0, 0)
        self.screen = screen
        self.textboxes = textboxes
        self.font = pygame.font.Font(st.FONT_PATH, 20)
        self.font_speaker = pygame.font.Font(st.FONT_PATH, 16)
        self.textbox_currently_typing = False
    
    def draw(self):
        # Create dialog box at the bottom of the screen
        dialog_rect = pygame.Rect(st.DIALOG_X, st.DIALOG_Y, st.DIALOG_WIDTH, st.DIALOG_HEIGHT)
        
        # Draw dialog box background with border
        pygame.draw.rect(self.screen, self.color, dialog_rect)
        script = pygame.transform.scale(sprites.SCRIPT, (st.DIALOG_WIDTH - st.DIALOG_SPEAKER_WIDTH, st.DIALOG_HEIGHT))
        script_rect = pygame.Rect(st.SCRIPT_X, st.DIALOG_Y, st.DIALOG_WIDTH - st.DIALOG_SPEAKER_WIDTH, st.DIALOG_HEIGHT)
        self.screen.blit(script, script_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), dialog_rect, 2)
        
        # Track current line being displayed
        if not hasattr(self, 'current_line'):
            self.current_line = 0
            self.display_complete = False
        
        # Display current line
        if self.current_line < len(self.textboxes):
            textbox = self.textboxes[self.current_line]
            textbox.draw(self.screen, self.display_complete)
            self.textbox_currently_typing = textbox.currently_typing
            return False  # Dialog not complete
        else:
            self.display_complete = True
            self.textbox_currently_typing = False
            return True  # Dialog complete
    
    def next_line(self):
        """Advance to the next line of dialog"""
        if hasattr(self, 'current_line'):
            self.current_line += 1
            self.draw()
    
    def update(self):
        """Update the dialog state"""
        self.textboxes[self.current_line].update(self.screen, self.display_complete)
        self.textbox_currently_typing = self.textboxes[self.current_line].currently_typing
