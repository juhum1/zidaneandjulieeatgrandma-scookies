from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self):
        self.currentHealth = self.maxHealth
        self.maxHealth = None
        self.damage = 50
        self.attackSpeed = 1
        self.speed = 1
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
        
