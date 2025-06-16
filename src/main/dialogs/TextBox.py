import pygame

from src.main import settings as st

class TextBox:
    def __init__(self, speaker, text):
        self.text = text
        self.speaker = speaker
        self.font = pygame.font.Font(st.FONT_PATH, 20)
        self.font_speaker = pygame.font.Font(st.FONT_PATH, 16)
        self.padding_x = 30
        self.padding_y = 20
        self.chars_displayed = 0
        self.last_update = pygame.time.get_ticks()
        self.typing_speed = 10  # milliseconds per character
        self.currently_typing = True

    def draw(self, screen, display_complete):
        speaker_img = pygame.image.load(f'{st.SPRITE_PATH}/speakers/{self.speaker}.png').convert()
        speaker_img = pygame.transform.scale(speaker_img, (st.DIALOG_SPEAKER_WIDTH, st.DIALOG_HEIGHT - 30))
        speaker_rect = pygame.Rect(st.DIALOG_X, st.DIALOG_Y, st.DIALOG_SPEAKER_WIDTH, st.DIALOG_HEIGHT - 30)
        screen.blit(speaker_img, speaker_rect)

        speaker_name_rect = pygame.Rect(st.DIALOG_X, st.DIALOG_Y + st.DIALOG_HEIGHT - 30, st.DIALOG_SPEAKER_WIDTH, 30)
        pygame.draw.rect(screen, (0, 0, 0), speaker_name_rect)
        speaker_name_surface = self.font_speaker.render(self.speaker, True, (219, 187, 153))
        speaker_name_x = st.DIALOG_X + (st.DIALOG_SPEAKER_WIDTH - speaker_name_surface.get_width()) // 2
        speaker_name_y = st.DIALOG_Y + st.DIALOG_HEIGHT - 28
        screen.blit(speaker_name_surface, (speaker_name_x, speaker_name_y))

        # Calculate the maximum width for text wrapping
        max_width = st.DIALOG_WIDTH - st.DIALOG_SPEAKER_WIDTH - self.padding_x
        
        # Split the text into words
        words = self.text.split()
        lines = []
        current_line = []
        current_width = 0
        
        # Build lines of text that fit within max_width
        for word in words:
            word_surface = self.font.render(word + " ", True, st.DEFAULT_DIALOG_COLOR)
            word_width = word_surface.get_width()
            
            if current_width + word_width <= max_width:
                current_line.append(word)
                current_width += word_width
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_width = word_width
        
        # Add the last line
        if current_line:
            lines.append(" ".join(current_line))

        # Create a surface tall enough for all lines
        line_height = self.font.get_linesize()
        text_surface = pygame.Surface((max_width, line_height * len(lines)), pygame.SRCALPHA)

        # Update characters displayed based on time
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.typing_speed and not display_complete:
            self.chars_displayed += 1
            self.last_update = current_time

        # Calculate total characters in all lines
        total_chars = sum(len(line) for line in lines)
        if not display_complete:
            chars_to_show = min(self.chars_displayed, total_chars)
        else:
            chars_to_show = total_chars

        # Display text character by character
        chars_shown = 0
        for i, line in enumerate(lines):
            if chars_shown >= chars_to_show:
                break
            
            # Calculate how many characters of this line to show
            chars_remaining = chars_to_show - chars_shown
            if chars_remaining > 0:
                display_text = line[:chars_remaining]
                # Split display text into words and render each with appropriate color
                words = display_text.split()
                line_surface = pygame.Surface((self.font.size(display_text)[0], self.font.get_height()), pygame.SRCALPHA)
                x_offset = 0
                
                for word in words:
                    if word in st.HIGHLIGHTED_WORDS:
                        color = st.HIGHLIGHTED_WORD_COLOR  # Color for highlighted words
                    else:
                        color = st.DEFAULT_DIALOG_COLOR  # Default color
                    
                    word_surface = self.font.render(word + " ", True, color)
                    line_surface.blit(word_surface, (x_offset, 0))
                    x_offset += word_surface.get_width()
                text_surface.blit(line_surface, (0, i * line_height))
            
            chars_shown += len(line)

        screen.blit(text_surface, (st.SCRIPT_X + self.padding_x, st.DIALOG_Y + self.padding_y))

        # Draw prompt indicator when text is complete
        if chars_shown >= total_chars:
            display_complete = True
            self.currently_typing = False
        
        # Draw prompt indicator
        if display_complete:
            prompt_image = pygame.image.load(f'{st.SPRITE_PATH}/enter.png').convert_alpha()
            prompt_image = pygame.transform.scale(prompt_image, (30, 30))
            prompt_rect = pygame.Rect(st.DIALOG_X + st.DIALOG_WIDTH - self.padding_x - 30, 
                                    st.DIALOG_Y + st.DIALOG_HEIGHT - self.padding_y - 30, 30, 30)
            screen.blit(prompt_image, prompt_rect)

        
    def update(self, screen, display_complete):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.typing_speed:
            self.chars_displayed += 1
            self.last_update = current_time
            self.draw(screen, display_complete)
