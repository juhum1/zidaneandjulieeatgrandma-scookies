from abc import ABC, abstractmethod
import pygame

class Tower(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.attackSpeed = 1
        self.range = 1
        self.lastAttackTime = 0  

    def can_attack(self):
        now = pygame.time.get_ticks()
        return (now - self.lastAttackTime) >= self.attackSpeed * 1000 # 1000 bc pygame time is in ms, essentially checking if enough time has passed since last attack

    def attack_enemy(self, enemy):
        if self.can_attack():
            if enemy.currentHealth > 0:
                enemy.currentHealth -= self.damage
                self.lastAttackTime = pygame.time.get_ticks()


class Classic(Tower):
    def __init__(self):
        self.maxHealth = 150
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth 
        self.sprite = "assets/classic.png"
        self.damage = 50
        self.range = 1
        self.attackSpeed = 1
        self.price = 100
        img = pygame.image.load(self.sprite).convert_alpha()
        rect = img.get_bounding_rect()
        cropped = img.subsurface(rect).copy()
        scale_factor = min(80 / rect.width, 80 / rect.height)
        new_size = (int(rect.width * scale_factor), int(rect.height * scale_factor))
        scaled = pygame.transform.smoothscale(cropped, new_size)
        centered = pygame.Surface((80, 80), pygame.SRCALPHA)
        offset_x = (80 - new_size[0]) // 2
        offset_y = (80 - new_size[1]) // 2
        centered.blit(scaled, (offset_x, offset_y))
        self.sprite_surface = centered
        


class Fast(Tower):
    def __init__(self):
        self.maxHealth = 100
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth
        self.sprite = "assets/tower.png"
        self.damage = 45
        self.range = 1
        self.attackSpeed = 2
        self.price = 150
        img = pygame.image.load(self.sprite).convert_alpha()
        rect = img.get_bounding_rect()
        cropped = img.subsurface(rect).copy()
        scale_factor = min(80 / rect.width, 80 / rect.height)
        new_size = (int(rect.width * scale_factor), int(rect.height * scale_factor))
        scaled = pygame.transform.smoothscale(cropped, new_size)
        centered = pygame.Surface((80, 80), pygame.SRCALPHA)
        offset_x = (80 - new_size[0]) // 2
        offset_y = (80 - new_size[1]) // 2
        centered.blit(scaled, (offset_x, offset_y))
        self.sprite_surface = centered
