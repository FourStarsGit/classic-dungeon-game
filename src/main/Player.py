import pygame
from src.main.room.Room import Room
from src.main import settings as st
import src.main.sprites as sprites

vec = pygame.math.Vector2

PLAYER_HIT_RECT = pygame.Rect(0, 0, int(st.TILE_SIZE * 0.8), int(st.TILE_SIZE * 0.6))

def collide_hit_rect(one, two):
    return one.rect.colliderect(two)

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__(*set())
        self.rect = pygame.Rect(st.SCREEN_WIDTH // 2, st.TILE_SIZE * 7, st.TILE_SIZE, st.TILE_SIZE)
        self.color  = st.WHITE
        self.appear = True
        self.facing_left = False
        self.attack_direction = "RIGHT"
        self.moving = False
        self.appear = True
        self.screen = screen
        self.pos = vec((st.SCREEN_WIDTH // 2, st.TILE_SIZE * 7))
        self.hit_rect = PLAYER_HIT_RECT
        self.vel = vec((4, 4))
        self.vel.x = st.PLAYER_SPEED
        self.vel.y = st.PLAYER_SPEED
        self.max_hearts = 6
        self.current_hearts = 3
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.invulnerable_duration = 2000
        self.frame_index = st.FRAME_INDEX
        self.frame_counter = 0
        self.frames = []
        self.attacking = False
        self.attack_timer = 0
        for i in range(8):  # 8 frames in the sprite sheet
            # Calculate the correct rectangle for each sprite
            sprite_rect = pygame.Rect(
                i * st.SPRITE_WIDTH,  # X position in sprite sheet
                0,                    # Y position (always 0 for single row)
                st.SPRITE_WIDTH,      # Width of single sprite
                st.SPRITE_HEIGHT      # Height of single sprite
            )
            # Extract and scale the sprite
            sprite = sprites.PLAYER_SHEET.subsurface(sprite_rect)
            scaled_sprite = pygame.transform.scale(sprite, (st.TILE_SIZE, st.TILE_SIZE))
            self.frames.append(scaled_sprite)
            self.frames_attack = []
        for i in range(5):  # 8 frames in the sprite sheet
            # Calculate the correct rectangle for each sprite
            sprite_rect = pygame.Rect(
                i * 65,  # X position in sprite sheet
                0,                    # Y position (always 0 for single row)
                65,      # Width of single sprite
                st.SPRITE_HEIGHT      # Height of single sprite
            )
            # Extract and scale the sprite
            sprite = sprites.PLAYER_ATTACK_SHEET.subsurface(sprite_rect)
            scaled_sprite = pygame.transform.scale(sprite, (st.TILE_SIZE, st.TILE_SIZE))
            self.frames_attack.append(scaled_sprite)

    def spawn(self):
        if self.appear and not self.attacking:
            if not self.moving:
                self.frame_index = 0  # Reset to standing frame when not moving
            self.frame = self.frames[self.frame_index]
            if self.facing_left:
                self.frame = pygame.transform.flip(self.frame, True, False)
            self.screen.blit(self.frame, self.rect)

    def collide_with_walls(self, walls, dir_):
        if dir_ == 'x':
            hits = pygame.sprite.spritecollide(self, walls, False, collide_hit_rect)
            if hits:
                # hit from left
                if hits[0].centerx > self.rect.centerx:
                    self.pos.x -= st.PLAYER_SPEED
                # hit from right
                elif hits[0].centerx < self.rect.centerx:
                    self.pos.x += st.PLAYER_SPEED

                self.vel.x = 0
                self.rect.centerx = self.pos.x

        elif dir_ == 'y':
            hits = pygame.sprite.spritecollide(self, walls, False, collide_hit_rect)
            if hits:
                # hit from top
                if hits[0].centery > self.rect.centery:
                    self.pos.y -= st.PLAYER_SPEED
                # hit from bottom
                elif hits[0].centery < self.rect.centery:
                    self.pos.y += st.PLAYER_SPEED

                self.vel.y = 0
                self.rect.centery = self.pos.y

    def key_press(self, keys, current_room: Room):
        used_event = False
        self.vel = vec(0, 0)
        self.moving = False  # Reset moving state

        if current_room.pre_dialog_shown and (current_room.post_dialog_shown ^ (current_room.boss is not None)):
            if keys[pygame.K_UP]:
                self.vel.y = -st.PLAYER_SPEED
                used_event = True
                self.attack_direction = "UP"
                self.moving = True

            if keys[pygame.K_DOWN]:
                self.vel.y = st.PLAYER_SPEED
                used_event = True
                self.attack_direction = "DOWN"
                self.moving = True

            if keys[pygame.K_LEFT]:
                self.vel.x = -st.PLAYER_SPEED
                used_event = True
                self.attack_direction = "LEFT"
                self.moving = True
                self.facing_left = True

            if keys[pygame.K_RIGHT]:
                self.vel.x = st.PLAYER_SPEED
                used_event = True
                self.attack_direction = "RIGHT"
                self.moving = True
                self.facing_left = False

            # Update animation only when moving
            if self.moving and not self.attacking:
                self.frame_counter += 1
                if self.frame_counter >= st.FRAME_SPEED:
                    self.frame_index = (self.frame_index + 1) % len(self.frames)
                    self.frame_counter = 0

        return used_event

    def hit(self, attacker_pos):
        if not self.invulnerable:
            self.invulnerable = True
            self.current_hearts -= 1
            self.invulnerable_timer = pygame.time.get_ticks()
            
            # Push player away from attacker
            direction = vec(self.pos - attacker_pos)
            if direction.length() > 0:
                direction = direction.normalize()
                self.pos += direction * 40  # Strong knockback
            
            return True
        return False
