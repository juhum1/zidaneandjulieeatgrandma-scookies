from abc import ABC, abstractmethod
import pygame

class Tower(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.attackSpeed = 1
        self.range = 1

    @abstractmethod
    def attack_enemy(self, enemy):
        enemy.currentHealth -= self.damage


class Classic(Tower):
    def __init__(self):
        self.maxHealth = 150
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
        
    
    def attack_enemy(self, enemy):
        super().attack_enemy(enemy)
        

class Fast(Tower):
    def __init__(self):
        self.maxHealth = 100
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

    def attack_enemy(self, enemy):
        super().attack_enemy(enemy)
