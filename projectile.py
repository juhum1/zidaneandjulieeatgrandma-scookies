import pygame
import math

class Projectile:
    def __init__(self, target_y, start_pos, target, damage, speed=100, range=1, sprite_path="assets/fireball.png", board=None, slow_factor: float = None, slow_duration: int = 0):

        self.x, self.y = start_pos
        self.start_y = start_pos[1]
        self.target_y = target_y
        self.range = range
        self.target = target 
        self.damage = damage
        self.speed = speed
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.alive = True
        self.slow_factor = slow_factor
        self.slow_duration = slow_duration

        distance = target_y - self.y
        if distance == 0:
            distance = 1  # Avoid division by zero
        self.dir_y = distance / abs(distance)

    def move(self):
        self.y += self.dir_y * self.speed

    def draw(self, screen):
        fireball = self.sprite.copy()
        screen.blit(fireball, (self.x, self.y))

    def check_collision(self, board):
        if self.target_y - self.y <= 0:
            distance = -1*( self.target_y - self.y)
            if self.damage == 25:  # if projectile slowing tower, slow the enemy as well
                self.target.speed *= 0.5 
            # attack enemy
            self.target.take_damage(self.damage, board)
            # ——— NEW: apply slow if provided ———
            if self.slow_factor is not None:
                self.target.apply_slow(self.slow_factor, self.slow_duration)
            return True
        return False
