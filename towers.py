from abc import ABC, abstractmethod
class Tower(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.attackSpeed = 1
        self.reach = 1


    @abstractmethod
    def attack(self, enemy):
        enemy.health -= self.damage
        if enemy.health <= 0:
            enemy.die()
        
    
class Classic(Tower):
    def __init__(self):
        self.maxHealth = 150
        self.currentHealth = self.maxHealth 
        self.sprite = sprite
        self.range = 1
        self.price = 100
    
    def attack(self, enemy):
        super().attack(enemy)
        


