import pygame
import math

class Projectile:
    """Creates a projectile that moves towards a target."""
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

        distance = target_y - self.y
        if distance == 0:
            distance = 1  # Avoid division by zero
        self.dir_y = distance / abs(distance)

    def move(self):
        self.y += self.dir_y * self.speed

    def draw(self, screen):
        fireball = self.sprite.copy()
        screen.blit(fireball, (self.x, self.y))

    def check_collision(self, board):   # takes board as an argument to access the target's position (used for bandit teleport)
        # Simple collision based on distance 
        distance = -1*( self.target_y - self.y)
        if distance <= 0:  
            self.target.take_damage(self.damage, board)
            return True
        return False
