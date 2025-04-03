from abc import ABC, abstractmethod
class Tower(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.attackSpeed = 1
        self.reach = 1


    @abstractmethod
    def attack_enemy(self, enemy):
        enemy.health -= self.damage

        
    
class Classic(Tower):
    def __init__(self):
        self.maxHealth = 150
        self.currentHealth = self.maxHealth 
        self.sprite = "assets/classic.png"
        self.range = 1
        self.price = 100
    
    def attack_enemy(self, enemy):
        super().attack(enemy)
        


