from abc import ABC, abstractmethod
import pygame
import projectile
def scale_image(img):
        rect = img.get_bounding_rect()
        scale_imageped = img.subsurface(rect).copy()
        scale_factor = min(80 / rect.width, 80 / rect.height)
        new_size = (int(rect.width * scale_factor), int(rect.height * scale_factor))
        scaled = pygame.transform.smoothscale(scale_imageped, new_size)
        centered = pygame.Surface((80, 80), pygame.SRCALPHA)
        offset_x = (80 - new_size[0]) // 2
        offset_y = (80 - new_size[1]) // 2
        centered.blit(scaled, (offset_x, offset_y))
        return centered


class Tower(ABC):
    def __init__(self):
        self.maxHealth = None
        self.currentHealth = self.maxHealth
        self.damage = 50
        self.attackSpeed = 1
        self.range = 1
        self.lastAttackTime = 0  


    def can_attack(self):
        now = pygame.time.get_ticks()
        return (now - self.lastAttackTime) >= 1000 / self.attackSpeed  # 1000 bc pygame time is in ms, essentially checking if enough time has passed since last attack

    def attack_enemy(self, enemy):
        if self.can_attack():



            if enemy.currentHealth > 0:
                enemy.currentHealth -= self.damage
                self.lastAttackTime = pygame.time.get_ticks()

    def shoot(self, enemy, board, i, j, k):
        if self.can_attack() and enemy.currentHealth > 0:
            new_proj = projectile.Projectile(
                start_pos=(j * board.tile_size, i * board.tile_size),
                target=enemy,
                damage=self.damage,
                range=self.range,
                target_y=k * board.tile_size,
                board=board
            )
            board.projectiles.append(new_proj)
            self.lastAttackTime = pygame.time.get_ticks()

class Classic(Tower):
    def __init__(self):
        print(f"Initializing tower: {self.__class__.__name__}")

        self.maxHealth = 150
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth 
        self.sprite = "assets/wizard_back.png"
        self.damage = 50
        self.range = 3
        self.attackSpeed = 1
        self.price = 100
        self.sprite_surface = scale_image(pygame.image.load(self.sprite).convert_alpha())

    @staticmethod
    def get_price():
        return 100

    @staticmethod
    def get_sprite_path():
        return "assets/wizard_back.png"


class Fast(Tower):
    def __init__(self):
        print(f"Initializing tower: {self.__class__.__name__}")

        self.maxHealth = 100
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth
        self.sprite = "assets/tower.png"
        self.damage = 40
        self.range = 2
        self.attackSpeed = 3
        self.price = 150
        self.sprite_surface = scale_image(pygame.image.load(self.sprite).convert_alpha())

    @staticmethod
    def get_price():
        return 150

    @staticmethod
    def get_sprite_path():
        return "assets/tower.png"

class Heavy(Tower):
    def __init__(self):
        self.maxHealth = 300
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth
        self.sprite = "assets/tower.png"
        self.damage = 100 
        self.range = 3
        self.attackSpeed = 0.5
        self.price = 150
        self.sprite_surface = scale_image(pygame.image.load(self.sprite).convert_alpha())

    @staticmethod
    def get_price():
        return 150

    @staticmethod
    def get_sprite_path():
        return "assets/tower.png"
