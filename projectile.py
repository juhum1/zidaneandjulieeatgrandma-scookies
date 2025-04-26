import pygame
import math

class Projectile:
    def __init__(self, start_pos, target, damage, speed=5, range=1, sprite_path="assets/fireball.png"):
        self.x, self.y = start_pos
        self.start_y = start_pos[1]
        self.range = range
        self.target = target  # The enemy or tower it's chasing
        self.damage = damage
        self.speed = speed
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.alive = True

        distance = target.y - self.y
        if distance == 0:
            distance = 1  # Avoid division by zero
        self.dir_x = dx / distance
        self.dir_y = dy / distance

    def move(self):
        self.y += self.dir_y * self.speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def check_collision(self):
        # Simple collision based on distance threshold
        distance = self.target.y - self.y
        if distance <= 0 or self.range >= self.y - self.start_y:  
            # attack enemy
            self.target.take_damage(self.damage)
            return True
        return False

