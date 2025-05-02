from abc import ABC, abstractmethod
import board
import random
import towers
import pygame

class Enemy(ABC):
    def __init__(self):
        self.maxHealth = 1
        self.currentHealth = self.maxHealth
        self.damage = 50
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 10
        self.sprite = None
        self.row = 0
        self.col = 0
        self.last_move_time = pygame.time.get_ticks()


    def attack_tower(self, tower):
        tower.currentHealth -= self.damage

    def die(self, board = None):
        return None

    def take_damage(self, damage: int, board = None):
        self.currentHealth -= damage

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 80 
        self.currentHealth = self.maxHealth
        self.damage = 40
        self.speed = 2 
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 10
        self.sprite = "assets/goblin1.png"


class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 20 
        self.currentHealth = self.maxHealth
        self.damage = 50
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 5
        self.sprite = "assets/skeleton.png"

class Witch(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 150
        self.currentHealth = self.maxHealth
        self.damage = 70
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 3
        self.currency = 10
        self.sprite = "assets/witch.png"


    def track_position(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def die(self, board=None):
        return Skeleton()

class Bat(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 10
        self.currentHealth = self.maxHealth
        self.damage = 50
        self.speed = 3  
        self.attackSpeed = 0.5
        self.attackRange = 1
        self.currency = 2
        self.sprite = "assets/bat.png"

class Bandit(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 160
        self.currentHealth = self.maxHealth
        self.damage = 30
        self.speed = 2
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 8
        self.sprite = "assets/bandit.png"


    def take_damage(self, damage: int, board): # teleports bandit if it takes damage
        self.currentHealth -= damage
        if board:
            old_row, old_col = self.row, self.col  
            valid_spots = []
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_r = self.row + dr
                    new_c = self.col + dc
                    if 0 <= new_r < board.rows and 0 <= new_c < board.cols:
                        if board.array[new_r][new_c].item is None:
                            valid_spots.append((new_r, new_c))
            if valid_spots:
                new_pos = random.choice(valid_spots)
                board.array[old_row][old_col].item = None 
                self.row, self.col = new_pos
                board.array[self.row][self.col].item = self

class Necromancer(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.damage = 20
        self.speed = 1
        self.attackSpeed = 1.5
        self.attackRange = 4
        self.currency = 15
        self.sprite = "assets/necromancer.png"

    def die(self, board=None):
        return [Skeleton(), Skeleton()]


class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 40
        self.currentHealth = self.maxHealth
        self.damage = 25
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 3
        self.sprite = "assets/slime.png"


    def die(self, board=None):
        return [Slimelet(), Slimelet()]

class Slimelet(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 10
        self.currentHealth = self.maxHealth
        self.damage = 10
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 1
        self.sprite = "assets/slimelet.png"


class FireImp(Enemy):
    def __init__(self):
        super().__init__()
        self.maxHealth = 50
        self.currentHealth = self.maxHealth
        self.damage = 35
        self.speed = 2
        self.attackSpeed = 0.8
        self.attackRange = 2
        self.currency = 12
        self.sprite = "assets/fire_spirit.png"



    def die(self, board=None):
        if board:
            next_row = self.row + 1
            tower = board.array[next_row][self.col].item if next_row < board.rows else None
            if tower and isinstance(tower, towers.Tower):
                board.array[next_row][self.col].item = None  # explodes tower
            
        return None
