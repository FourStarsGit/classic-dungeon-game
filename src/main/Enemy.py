import pygame
import random
import math
from src.main import settings as st, sprites
from pygame.math import Vector2 as vec
from enum import Enum

def collide_hit_rect(one, two):
    return one.rect.colliderect(two)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, enemy_type, life=1):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, st.TILE_SIZE, st.TILE_SIZE)
        self.enemy_type = enemy_type
        self.color = (255, 0, 0)  # Base color
        self.pos = vec((x, y))
        self.vel = vec(0, 0)
        self.speed = 2
        self.movement_timer = 0
        self.movement_delay = 1000  # Change direction every 1 second
        self.life = life
        
        # Animation states
        self.being_hit = False
        self.hit_timer = 0
        self.hit_duration = 200
        
    def random_movement(self):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.movement_timer > self.movement_delay:
            # Change direction randomly
            angle = random.uniform(0, 2 * math.pi)
            self.vel.x = math.cos(angle) * self.speed
            self.vel.y = math.sin(angle) * self.speed
            self.movement_timer = current_time

    def collide_with_walls(self, walls, dir_):
        if dir_ == 'x':
            hits = pygame.sprite.spritecollide(self, walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:  # Moving right
                    self.pos.x = hits[0].left - self.rect.width
                elif self.vel.x < 0:  # Moving left
                    self.pos.x = hits[0].right
                self.vel.x *= -1  # Reverse direction when hitting wall
                self.rect.x = self.pos.x
        elif dir_ == 'y':
            hits = pygame.sprite.spritecollide(self, walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:  # Moving down
                    self.pos.y = hits[0].top - self.rect.height
                elif self.vel.y < 0:  # Moving up
                    self.pos.y = hits[0].bottom
                self.vel.y *= -1  # Reverse direction when hitting wall
                self.rect.y = self.pos.y

    def collide_with_player(self, player):
        if self.rect.colliderect(player.rect):
            # Push enemy away from player
            direction = vec(self.pos - player.pos)
            if direction.length() > 0:
                direction = direction.normalize()
                self.pos += direction * self.speed
                return True
        return False
            
    def update(self, player_pos, walls):
        # Execute random movement
        self.random_movement()
        
        # Update position with wall collisions
        self.pos.x += self.vel.x
        self.rect.x = self.pos.x
        self.collide_with_walls(walls, 'x')
        
        self.pos.y += self.vel.y
        self.rect.y = self.pos.y
        self.collide_with_walls(walls, 'y')
        
        # Keep enemy within screen bounds
        self.pos.x = max(st.TILE_SIZE + st.TILE_SIZE // 2, min(self.pos.x, st.SCREEN_WIDTH - st.TILE_SIZE - st.TILE_SIZE // 2))
        self.pos.y = max(st.TILE_SIZE + st.TILE_SIZE // 2, min(self.pos.y, st.SCREEN_HEIGHT - st.TILE_SIZE - st.TILE_SIZE // 2))
        
        # Update rect position
        self.rect.center = self.pos
        
        # Update hit animation
        if self.being_hit:
            current_time = pygame.time.get_ticks()
            if current_time - self.hit_timer > self.hit_duration:
                self.being_hit = False
                
    def hit(self):
        if not self.being_hit:
            self.being_hit = True
            self.hit_timer = pygame.time.get_ticks()
            st.ENEMY_HIT_SOUND.play()
            self.life -= 1
        return self.life <= 0
        
    def spawn(self):
        self.screen.blit(self.enemy_type.value, self.rect)


class EnemyType(Enum):
    MAIZE = sprites.ENEMY_MAIZE
    DEMON = sprites.ENEMY_DEMON
    PAPER = sprites.ENEMY_PAPER


class EnemyMaize(Enemy):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen, EnemyType.MAIZE, life=1)
        self.enemy_type = EnemyType.MAIZE

class EnemyDemon(Enemy):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen, EnemyType.DEMON, life=2)
        self.enemy_type = EnemyType.DEMON
    
    def spawn(self):
        current_frame = (pygame.time.get_ticks() // 200) % 4  # Change frame every 200ms
        self.screen.blit(self.enemy_type.value[current_frame], self.rect)

class EnemyPaper(Enemy):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen, EnemyType.PAPER, life=3)
        self.enemy_type = EnemyType.PAPER