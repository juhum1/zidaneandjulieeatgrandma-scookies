from abc import ABC, abstractmethod

class Tower(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.attackSpeed = 1
        self.range = 1

    @abstractmethod
    def attack_enemy(self, enemy):
        enemy.health -= self.damage

class Classic(Tower):
    def __init__(self):
        self.maxHealth = 150
        self.currentHealth = self.maxHealth 
        self.sprite = "assets/classic.png"
        self.damage = 50
        self.range = 1
        self.attackSpeed = 1
        self.price = 100
    
    def attack_enemy(self, enemy):
        super().attack_enemy(enemy)
        

class Fast(Tower):
    def __init__(self):
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.sprite = "assets/tower.png"
        self.range = 1
        self.attackSpeed = 2
        self.price = 150

    def attack_enemy(self, enemy):
        super().attack_enemy(enemy)
