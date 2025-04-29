import pygame
import math

class Projectile:
    def __init__(self, target_y, start_pos, target, damage, speed=30, range=1, sprite_path="assets/fireball.png"):

        self.x, self.y = start_pos
        self.start_y = start_pos[1]
        self.target_y = target_y
        self.range = range
        self.target = target  # The enemy or tower it's chasing
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
        fireball.set_alpha(150)  # from 0 (invisible) to 255 (fully visible)
        screen.blit(fireball, (self.x, self.y))

    def check_collision(self):
        # Simple collision based on distance threshold
        #find target y from 

        distance = -1*( self.target_y - self.y)
        if distance <= 0:  
            # attack enemy
            self.target.take_damage(self.damage)
            return True
        return False

