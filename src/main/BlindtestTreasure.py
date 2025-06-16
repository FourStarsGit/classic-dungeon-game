import pygame
from src.main import settings as st, sprites

class BlindtestTreasure:

    def __init__(self):
        self.current_question = 0
        self.previous_question = None
        self.score = 0
        self.questions = [
            {
                "menu_text" : "De quel dessin animé il s'agit ?",
                "sound": st.TOTALLY_SPIES_SOUND,
                "choices": ["Kim Possible", "Les Supers Nanas", "Ben 10", "Totally Spies"],
                "correct": 3
            },
            {
                "menu_text" : "Bravo ! Deuxième extrait...",
                "sound": st.KIM_POSSIBLE_SOUND,
                "choices": ["Kim Possible", "Sonic", "Danny fantôme", "Winx club"],
                "correct": 0
            },
            {
                "menu_text" : "2 bonnes réponses ! Continue !",
                "sound": st.CODE_LYOKO_SOUND,
                "choices": ["Pokémon", "Franklin", "Code Lyoko", "Les Supers Nanas"],
                "correct": 2
            },
            {
                "menu_text" : "On saura sauver notre existence !",
                "sound": st.WINX_CLUB_SOUND,
                "choices": ["Petit ours brun", "Maya l'abeille", "Digimon", "Winx Club"],
                "correct": 3
            },
            {
                "menu_text" : "On cherche une série...",
                "sound": st.GAME_OF_THRONES_SOUND,
                "choices": ["Stranger things", "Game Of Thrones", "House of dragons", "Suits"],
                "correct": 1
            },
            {
                "menu_text" : "Autre série !",
                "sound": st.PLUS_BELLE_LA_VIE_SOUND,
                "choices": ["Plus belle la vie", "Foudre", "Un si grand soleil", "Friends"],
                "correct": 0
            },
            {
                "menu_text" : "La musique d'un film maintenant !",
                "sound": st.FULL_MONTY_SOUND,
                "choices": ["Sister Act", "Dirty Dancing", "Grease", "Full Monty"],
                "correct": 3
            },
            {
                "menu_text" : "Plus que 3 questions !",
                "sound": st.KOH_LANTA_SOUND,
                "choices": ["The Voice", "Koh Lanta", "Secret Story", "Pékin express"],
                "correct": 1
            },
            {
                "menu_text" : "On revient sur les dessins animés",
                "sound": st.INSPECTEUR_GADGET_SOUND,
                "choices": ["Les Supers Nanas", "La panthère rose", "Kid Paddle", "Inspecteur Gadget"],
                "correct": 3
            },
            {
                "menu_text" : "ATTENTION ! DERNIÈRE QUESTION !",
                "sound": st.ASTERIX_ET_CLEOPATRE_SOUND,
                "choices": ["Astérix et ...", "Les Supers Nanas", "Mulan", "Sonic"],
                "correct": 0
            },
        ]
        self.is_active = False
        self.selected_choice = 0
        self.last_key_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(st.FONT_PATH, 25)
        self.font_mini = pygame.font.Font(st.FONT_PATH, 16)
        self.potential_points = 5
        self.show_validate = False
        self.show_error = False
        self.validate_start_time = 0
        self.error_start_time = 0
        self.end_game_start_time = 0

        
    def start_blindtest(self):        
        # Store the start time when menu is shown
        self.menu_start_time = pygame.time.get_ticks()
        self.is_active = True
    
    def draw_blindtest(self, screen):
        if not self.is_active:
            return

        # Check if 10 seconds have passed
        if pygame.time.get_ticks() - self.menu_start_time < 10000:
            if not pygame.mixer.get_busy():
                st.BACKGROUND_SOUND.play(-1)
            # Draw dialog box background with border
            script = pygame.transform.scale(sprites.SCRIPT, (st.DIALOG_WIDTH, 250))
            script_rect = pygame.Rect(st.DIALOG_X, st.SCREEN_HEIGHT // 2, st.DIALOG_WIDTH, 400)
            st.SCREEN.blit(script, script_rect)
            menu_rect = pygame.Rect(st.DIALOG_X, st.SCREEN_HEIGHT // 2, st.DIALOG_WIDTH, 400)
            pygame.draw.rect(st.SCREEN, st.DEFAULT_DIALOG_COLOR, menu_rect, 2)
            menu_text_1 = self.font.render("Bienvenue dans ce blindtest ! Sauras-tu", True, st.DEFAULT_DIALOG_COLOR)
            menu_text_2 = self.font.render("retrouver toutes ces références ?", True, st.DEFAULT_DIALOG_COLOR)
            menu_text_3 = self.font.render("Bonne chance !", True, st.DEFAULT_DIALOG_COLOR)
            menu_text_4 = self.font.render("5 points si tu trouves du 1er coup,", True, st.DEFAULT_DIALOG_COLOR)
            menu_text_5 = self.font.render("3 points pour deux coups", True, st.DEFAULT_DIALOG_COLOR)
            menu_text_6 = self.font.render("et 1 point sinon. Démarrage en cours...", True, st.DEFAULT_DIALOG_COLOR)
            line_height = self.font.get_linesize()
            st.SCREEN.blit(menu_text_1, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 + line_height))
            st.SCREEN.blit(menu_text_2, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 2)))
            st.SCREEN.blit(menu_text_3, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 3)))
            st.SCREEN.blit(menu_text_4, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 4)))
            st.SCREEN.blit(menu_text_5, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 5)))
            st.SCREEN.blit(menu_text_6, (st.DIALOG_X + 35, (st.SCREEN_HEIGHT // 2 + line_height * 6)))
            
        else:
            st.BACKGROUND_SOUND.stop()
            if self.current_question != self.previous_question:
                if self.previous_question != None:
                    self.questions[self.previous_question]["sound"].stop()
                self.previous_question = self.current_question
                self.questions[self.current_question]["sound"].play(-1)
            # Draw dialog box statement
            script = pygame.transform.scale(sprites.SCRIPT, (st.DIALOG_WIDTH, 400))
            screen.blit(script, (st.DIALOG_X, st.SCREEN_HEIGHT // 3))

            # Draw statement text
            statement_text = self.font.render(self.questions[self.current_question]["menu_text"], True, st.DEFAULT_DIALOG_COLOR)
            screen.blit(statement_text, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 - 35))

            # Draw semi-transparent black background for choices
            choices_surface = pygame.Surface((st.DIALOG_WIDTH // 2 - 85, 160))
            choices_surface.fill((0, 0, 0))
            choices_surface.set_alpha(150)
            screen.blit(choices_surface, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 + 35))
            # Draw choices
            for i, choice in enumerate(self.questions[self.current_question]["choices"]):
                color = st.WHITE if i == self.selected_choice else st.BLACK
                text = self.font.render(choice, True, color)
                screen.blit(text, (st.DIALOG_X + 35, st.SCREEN_HEIGHT // 2 + 35 + i * 40))

            explanations = f"5 points si tu trouves du 1er coup,\n3 points pour deux coups \net 1 point sinon."
            for i, row in enumerate(explanations.split('\n')):
                text = self.font_mini.render(row, True, st.DEFAULT_DIALOG_COLOR)
                screen.blit(text, (st.SCREEN_WIDTH // 2 - 35, st.SCREEN_HEIGHT // 2 + 35 + i * 30))
            potential_points_text = self.font_mini.render(f"Points potentiels : {self.potential_points}", True, st.BLACK)
            screen.blit(potential_points_text, (st.SCREEN_WIDTH // 2 - 35, st.SCREEN_HEIGHT // 2 + 35 + 40 * 3))
            score_text = self.font_mini.render(f"Score actuel : {self.score}", True, (100, 190, 83))
            screen.blit(score_text, (st.SCREEN_WIDTH // 2 - 35, st.SCREEN_HEIGHT // 2 + 35 + 40 * 4))
            # Load and display validate sign
            if self.show_validate: 
                validate_rect = sprites.VALIDATE_SIGN.get_rect(bottomright=(st.SCREEN_WIDTH - 20, st.SCREEN_HEIGHT - 20))
                st.SCREEN.blit(sprites.VALIDATE_SIGN, validate_rect)
            elif self.show_error:
                error_rect = sprites.ERROR_SIGN.get_rect(bottomright=(st.SCREEN_WIDTH - 20, st.SCREEN_HEIGHT - 20))
                st.SCREEN.blit(sprites.ERROR_SIGN, error_rect)
            
            # Check if 1.5 seconds have passed to hide the signs
            if pygame.time.get_ticks() - self.validate_start_time > 1500:
                self.show_validate = False
            if pygame.time.get_ticks() - self.error_start_time > 1500:
                self.show_error = False
    
    def handle_input(self, event):
        if not self.is_active:
            return False
        elif pygame.time.get_ticks() - self.menu_start_time < 10000:
            return True
            
        # Add key repeat delay to prevent too sensitive keyboard input
        if event.type == pygame.KEYDOWN and pygame.time.get_ticks() - self.last_key_time > 200:
            self.last_key_time = pygame.time.get_ticks()
            if event.key == pygame.K_UP:
                self.selected_choice = (self.selected_choice - 1) % 4
                st.MENU_MOVE_SOUND.play()
            elif event.key == pygame.K_DOWN:
                self.selected_choice = (self.selected_choice + 1) % 4
                st.MENU_MOVE_SOUND.play()
            elif event.key == pygame.K_RETURN:
                correct = self.selected_choice == self.questions[self.current_question]["correct"]
                if correct:
                    self.score += self.potential_points
                    self.potential_points = 5
                    self.current_question += 1
                    st.CORRECT_ANSWER_SOUND.play()
                    # Set the validation sign display time
                    self.validate_start_time = pygame.time.get_ticks()
                    self.show_validate = True
                else:
                    st.WRONG_ANSWER_SOUND.play()
                    # Set the error sign display time
                    self.error_start_time = pygame.time.get_ticks()
                    self.show_error = True
                    self.potential_points = max(1, self.potential_points - 2)
                self.is_active = self.current_question < len(self.questions)
                if not self.is_active:
                    self.questions[self.previous_question]["sound"].stop()
                    st.APPLAUSE_SOUND.play()
                return self.is_active
        return True