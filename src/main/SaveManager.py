import json
import os
import pygame
from src.main import settings as st

class SaveManager:
    def __init__(self):
        self.save_file = "save_data.json"
        self.default_save = {
            "current_room_index": 0,  # Index in the rooms list
            "hearts": 3,
            "has_save": False,
            "enemies_defeated": {},  # Dictionary to track number of defeated enemies per room
            "room_states": {}  # Dictionary to track room states (doors open/closed)
        }
        
        # Create saves directory if it doesn't exist
        os.makedirs("saves", exist_ok=True)
        self.save_path = os.path.join("saves", self.save_file)
        
        # Save indicator properties
        self.font = pygame.font.Font(None, 24)
        self.indicator_duration = 1500  # 1.5 seconds
        self.indicator_start = 0
        self.indicator_alpha = 255
        self.fade_speed = 3
        
        # Initialize save file if it doesn't exist
        if not os.path.exists(self.save_path):
            self.save_game(self.default_save)

    def save_game(self, save_data):
        """Save game data to file"""
        save_data["has_save"] = True
        with open(self.save_path, 'w') as f:
            json.dump(save_data, f)
        self.indicator_start = pygame.time.get_ticks()
        self.indicator_alpha = 255

    def load_game(self):
        """Load game data from file"""
        try:
            with open(self.save_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return self.default_save

    def has_save(self):
        """Check if there's a valid save file"""
        save_data = self.load_game()
        return save_data.get("has_save", False)

    def delete_save(self):
        """Delete the save file"""
        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def draw_save_indicator(self, screen):
        """Draw a save indicator that fades out"""
        current_time = pygame.time.get_ticks()
        if current_time - self.indicator_start < self.indicator_duration:
            # Create text surface
            text_surface = self.font.render("Sauvegarde...", True, (255, 255, 255))
            text_rect = text_surface.get_rect(bottomright=(st.SCREEN_WIDTH - 10, st.SCREEN_HEIGHT - 10))
            
            # Create alpha surface
            alpha_surface = pygame.Surface(text_surface.get_rect().size, pygame.SRCALPHA)
            alpha_surface.fill((255, 255, 255, self.indicator_alpha))
            
            # Blit with alpha
            text_surface.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(text_surface, text_rect)
            
            # Fade out
            self.indicator_alpha = max(0, self.indicator_alpha - self.fade_speed) 