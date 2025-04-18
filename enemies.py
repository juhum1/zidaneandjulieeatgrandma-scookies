from abc import ABC, abstractmethod
import board

class Enemy(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 10
        self.sprite = None

    @abstractmethod
    def attack_tower(self, tower):
        tower.currentHealth -= self.damage

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.die()

class Goblin(Enemy):
    def __init__(self):
        self.maxHealth = 50 
        self.currentHealth = self.maxHealth
        self.damage = 20
        self.speed = 2 
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 10
        self.sprite = "assets/goblin.png"

    def die(self):
        pass

    def attack_tower(self, tower):
        super().attack_tower(tower)

    def take_damage(self, damage: int):
        super().take_damage(damage)

class Skeleton(Enemy):
    def __init__(self):
        self.maxHealth = 20 
        self.currentHealth = self.maxHealth
        self.damage = 10
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 5
        self.sprite = "assets/skeleton.png"
    
    
class Witch(Enemy):
    def __init__(self):
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.damage = 40
        self.speed = 1
        self.attackSpeed = 1
        self.attackRange = 3
        self.currency = 10
        self.sprite = "assets/witch.png"

    def die(self, col): #skeleton(s) spawn when witch dies
        board.add(enemy, Skeleton(), col)

    def take_damage(self, damage: int):
        super().take_damage(damage)
