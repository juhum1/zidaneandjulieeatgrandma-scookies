from abc import ABC, abstractmethod
class Tower(ABC):
    def __init__(self, currentHealth, maxHealth, damage, attackSpeed, reach):
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.damage = damage
        self.attackSpeed = attackSpeed
        self.reach = reach

    @abstractmethod
    def attack(self, enemy):
        enemy.health -= 
        
    
class Classic(Tower):
    def attack(self
