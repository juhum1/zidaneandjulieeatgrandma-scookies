import pygame
import math

class Projectile:
    def __init__(self, target_y, start_pos, target, damage, speed=5, range=1, sprite_path="assets/fireball.png"):

        self.x, self.y = start_pos
        self.start_y = start_pos[1]
        self.target_y = target_y
        self.range = range
        self.target = target  # The enemy or tower it's chasing
        self.damage = damage
        self.speed = speed
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.alive = True
        print(f"🎯 projectile created at ({self.x}, {self.y}) with target {self.target_y}")

        distance = target_y - self.y
        if distance == 0:
            distance = 1  # Avoid division by zero
        self.dir_y = distance / abs(distance)

    def move(self):
        self.y += self.dir_y * self.speed
        print(f"🚀 projectile moved to ({self.x}, {self.y})")

    def draw(self, screen):
        print(f"🖼️ drawing projectile at ({self.x}, {self.y})")
        screen.blit(self.sprite, (self.x, self.y))

    def check_collision(self):
        # Simple collision based on distance threshold
        #find target y from 

        distance = -1*( self.target_y - self.y)
        if distance <= 0:  
            # attack enemy
            self.target.take_damage(self.damage)
            return True
        return False

