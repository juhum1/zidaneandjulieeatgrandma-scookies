from abc import ABC, abstractmethod
import pygame
import enemies
import projectile

def scale_image(img):
    """Scales all tower images to fit within a 80x80 pixel square while maintaining aspect ratio."""
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
    """Abstract base class for all towers."""
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

        self.maxHealth = 150
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth 
        self.sprite = "assets/wizard_back.png"
        self.damage = 40
        self.range = 2
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
        self.sprite = "assets/heavy.png"
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
        return "assets/heavy.png"

class Princess(Tower):
    def __init__(self):
        self.maxHealth = 75
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth
        self.sprite = "assets/princess_back.png"
        self.damage = 300 
        self.range = 6
        self.attackSpeed = 0.2
        self.price = 250
        self.sprite_surface = scale_image(pygame.image.load(self.sprite).convert_alpha())

    @staticmethod
    def get_price():
        return 250

    @staticmethod
    def get_sprite_path():
        return "assets/princess.png"

            
class Bomb(Tower):
    def __init__(self):
        self.maxHealth = 150
        self.lastAttackTime = 0 
        self.currentHealth = self.maxHealth
        self.sprite = "assets/bomb_tower.png"
        self.damage = 75 
        self.range = 2
        self.attackSpeed = 0.8
        self.price = 200
        self.sprite_surface = scale_image(pygame.image.load(self.sprite).convert_alpha())
    
    @staticmethod
    def get_price():
        return 200

    @staticmethod
    def get_sprite_path():
        return "assets/bomb_tower.png"

    def shoot(self, enemy, board, i, j, k):
        if self.can_attack():
            enemies_hit = []
            for col_offset in [-1, 0, 1]:
                col = j + col_offset
                if 0 <= col < board.cols:
                    target = board.array[k][col].item
                    if isinstance(target, enemies.Enemy) and target.currentHealth > 0:
                        enemies_hit.append(target)

            for target in enemies_hit:
                new_proj = projectile.Projectile(
                    start_pos=(j * board.tile_size, i * board.tile_size),
                    target=target,
                    damage=self.damage,
                    range=self.range,
                    target_y=k * board.tile_size,
                    board=board
                )
                board.projectiles.append(new_proj)

            self.lastAttackTime = pygame.time.get_ticks()
