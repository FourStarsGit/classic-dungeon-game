import pygame
from src.main import settings as st, sprites

class TitleGame:
    def __init__(self):
        self.is_active = False
        self.keyboard = [
            "AZERTYUIOP",
            "QSDFGHJKLM",
            "  WXCVBN  "
        ]
        self.current_row = 0
        self.current_col = 0
        self.typed_text = ""
        self.correct_answer = "TITRE"
        self.font = pygame.font.Font(st.FONT_PATH, 25)
        self.font_mini = pygame.font.Font(st.FONT_PATH, 16)
        self.last_key_time = pygame.time.get_ticks()
        self.show_validate = False
        self.validate_start_time = 0

    def start(self):
        self.is_active = True
        self.typed_text = ""
        
    def draw(self):
        if not self.is_active:
            return

        script = pygame.transform.scale(sprites.SCRIPT, (st.DIALOG_WIDTH, 400))
        script_rect = pygame.Rect(st.DIALOG_X, st.SCREEN_HEIGHT // 2 - 150, st.DIALOG_WIDTH, 400)
        st.SCREEN.blit(script, script_rect)
        menu_rect = pygame.Rect(st.DIALOG_X, st.SCREEN_HEIGHT // 2 - 150, st.DIALOG_WIDTH, 400)
        pygame.draw.rect(st.SCREEN, st.DEFAULT_DIALOG_COLOR, menu_rect, 2)
        line_height = self.font.get_linesize()

        # Draw question
        question_1 = self.font.render("Regardez bien le nom de la salle !!", True, st.DEFAULT_DIALOG_COLOR)
        question_2 = self.font.render("En 5 lettres, ceci est un...", True, st.DEFAULT_DIALOG_COLOR)
        st.SCREEN.blit(question_1, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 - 135 + line_height))
        st.SCREEN.blit(question_2, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 - 135 + line_height * 2))

        # Draw typed text
        typed_surface = self.font.render(self.typed_text, True, st.BLACK)
        st.SCREEN.blit(typed_surface, (st.SCREEN_WIDTH // 2 - typed_surface.get_width()//2, 350))

        # Draw keyboard
        key_size = 40
        spacing = 10
        start_y = st.SCREEN_HEIGHT // 2 + 35

        for row_idx, row in enumerate(self.keyboard):
            start_x = st.SCREEN_WIDTH//2 - (len(row) * (key_size + spacing))//2
            for col_idx, letter in enumerate(row):
                key_rect = pygame.Rect(start_x + col_idx * (key_size + spacing),
                                     start_y + row_idx * (key_size + spacing),
                                     key_size, key_size)
                
                # Highlight selected key
                color = st.YELLOW if (row_idx == self.current_row and 
                                    col_idx == self.current_col) else st.WHITE
                pygame.draw.rect(st.SCREEN, color, key_rect)
                pygame.draw.rect(st.SCREEN, st.BLACK, key_rect, 2)
                
                # Draw letter
                letter_surface = self.font_mini.render(letter, True, st.BLACK)
                letter_pos = (key_rect.centerx - letter_surface.get_width()//2,
                            key_rect.centery - letter_surface.get_height()//2)
                st.SCREEN.blit(letter_surface, letter_pos)

    def handle_input(self, event):
        if not self.is_active:
            return False

        if event.type == pygame.KEYDOWN and pygame.time.get_ticks() - self.last_key_time > 200:
            self.last_key_time = pygame.time.get_ticks()
            
            if event.key == pygame.K_LEFT:
                self.current_col = (self.current_col - 1) % len(self.keyboard[self.current_row])
                st.MENU_MOVE_SOUND.play()
            elif event.key == pygame.K_RIGHT:
                self.current_col = (self.current_col + 1) % len(self.keyboard[self.current_row])
                st.MENU_MOVE_SOUND.play()
            elif event.key == pygame.K_UP:
                self.current_row = (self.current_row - 1) % len(self.keyboard)
                self.current_col = min(self.current_col, len(self.keyboard[self.current_row]) - 1)
                st.MENU_MOVE_SOUND.play()
            elif event.key == pygame.K_DOWN:
                self.current_row = (self.current_row + 1) % len(self.keyboard)
                self.current_col = min(self.current_col, len(self.keyboard[self.current_row]) - 1)
                st.MENU_MOVE_SOUND.play()
            elif event.key == pygame.K_RETURN:
                # Add selected letter
                selected_letter = self.keyboard[self.current_row][self.current_col]
                self.typed_text += selected_letter
                st.MENU_SELECT_SOUND.play()
                
                # Check if answer is correct
                if self.typed_text == self.correct_answer:
                    st.CORRECT_ANSWER_SOUND.play()
                    self.is_active = False
                    return False
                elif len(self.typed_text) >= len(self.correct_answer):
                    st.WRONG_ANSWER_SOUND.play()
                    self.typed_text = ""
            elif event.key == pygame.K_BACKSPACE:
                if self.typed_text:
                    self.typed_text = self.typed_text[:-1]
                    st.MENU_BACK_SOUND.play()

        return True