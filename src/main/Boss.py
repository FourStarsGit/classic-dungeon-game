import pygame
from pygame.math import Vector2 as vec
from src.main import settings as st, sprites
from enum import Enum

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, st.TILE_SIZE * 1.5, st.TILE_SIZE * 1.5)  # Bigger than regular enemies
        self.pos = vec((x, y))
        self.vel = vec(0, 0)
        self.speed = 3
        self.is_vulnerable = False
        self.mode_timer = 0
        self.mode_duration = 3000  # Switch modes every 3 seconds
        self.health = 3
        self.being_hit = False
        self.hit_timer = 0
        self.hit_duration = 2000
        self.give_hearts = 4
        
    def update(self, player_pos, walls):
        current_time = pygame.time.get_ticks()
        self.player_pos = player_pos  # Store player position for hit method
        
        # Switch modes
        if current_time - self.mode_timer > self.mode_duration:
            self.is_vulnerable = not self.is_vulnerable
            if not self.is_vulnerable:
                st.BOSS_ATTACK_SOUND.play()
            self.mode_timer = current_time
        
        # Movement behavior
        if not self.is_vulnerable:
            # Attack mode: Move towards player
            direction = vec(player_pos) - self.pos
            if direction.length() > 0:
                direction = direction.normalize()
                self.vel = direction * self.speed
        else:
            # Vulnerable mode: Move away from player
            direction = self.pos - vec(player_pos)
            if direction.length() > 0:
                direction = direction.normalize()
                self.vel = direction * (self.speed * 0.5)  # Slower when vulnerable
        
        # Update position
        self.pos += self.vel
        
        # Keep within screen bounds
        self.pos.x = max(st.TILE_SIZE + st.TILE_SIZE // 4, min(self.pos.x, st.SCREEN_WIDTH - st.TILE_SIZE - st.TILE_SIZE // 4))
        self.pos.y = max(st.TILE_SIZE + st.TILE_SIZE // 4, min(self.pos.y, st.SCREEN_HEIGHT - st.TILE_SIZE - st.TILE_SIZE // 4))
        
        self.rect.center = (int(self.pos.x), int(self.pos.y))
        
        # Update hit animation
        if self.being_hit:
            if current_time - self.hit_timer > self.hit_duration:
                self.being_hit = False
    
    def hit(self):
        if self.is_vulnerable and not self.being_hit:
            self.being_hit = True
            self.hit_timer = pygame.time.get_ticks()
            st.ENEMY_HIT_SOUND.play()
            self.health -= 1
            
            # Push boss away from player
            direction = vec(self.pos - self.player_pos)
            if direction.length() > 0:
                direction = direction.normalize()
                self.pos += direction * 50  # Push distance
            
            return True
        return False
    
    def collide_with_player(self, player):
        if self.rect.colliderect(player.rect) and not self.is_vulnerable:
            # Push player away
            direction = vec(player.pos - self.pos)
            if direction.length() > 0:
                direction = direction.normalize()
                direction = direction * 20
                # Calculate new position while keeping player within bounds
                new_x = max(st.TILE_SIZE + st.TILE_SIZE // 4, 
                          min(player.pos.x + direction.x, 
                              st.SCREEN_WIDTH - st.TILE_SIZE - st.TILE_SIZE // 4))
                new_y = max(st.TILE_SIZE + st.TILE_SIZE // 4,
                          min(player.pos.y + direction.y,
                              st.SCREEN_HEIGHT - st.TILE_SIZE - st.TILE_SIZE // 4))
                player.pos.x = new_x
                player.pos.y = new_y
            return True
        return False
    
    def spawn(self):
        if self.being_hit:
            color = (255, 255, 255)  # Flash white when hit
        elif self.is_vulnerable:
            color = (0, 255, 0)  # Green in vulnerable mode
        else:
            color = (255, 0, 0)  # Red in attack mode
        pygame.draw.rect(self.screen, color, self.rect)

class CapitaineFracasse(Boss):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)

    def spawn(self):
        sprite = sprites.CAPITAINE_FRACASSE.copy()
        if self.being_hit:
            pass
        elif self.is_vulnerable:
            sprite.fill((0, 75, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        if not self.is_vulnerable:
            sprite.fill((75, 0, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        self.screen.blit(sprite, self.rect)


class Beetle(Boss):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.health = 5
        self.give_hearts = 5

    def spawn(self):
        sprite = sprites.BEETLE.copy()
        if self.being_hit:
            pass
        elif self.is_vulnerable:
            sprite.fill((0, 75, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        if not self.is_vulnerable:
            sprite.fill((75, 0, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        self.screen.blit(sprite, self.rect)

class Python(Boss):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.health = 5
        self.give_hearts = 6

    def spawn(self):
        sprite = sprites.PYTHON.copy()
        if self.being_hit:
            pass
        elif self.is_vulnerable:
            sprite.fill((0, 75, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        if not self.is_vulnerable:
            sprite.fill((75, 0, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        self.screen.blit(sprite, self.rect)

class OldDemon(Boss):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.health = 7
        self.give_hearts = 6

    def spawn(self):
        sprite = sprites.OLD_DEMON.copy()
        if self.being_hit:
            pass
        elif self.is_vulnerable:
            sprite.fill((0, 75, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        if not self.is_vulnerable:
            sprite.fill((75, 0, 0, 100), special_flags=pygame.BLEND_RGB_ADD)
        self.screen.blit(sprite, self.rect)