from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.health = health
        self.attack = attack

    @abstractmethod
    def attack_player(self):
        pass

    @abstractmethod
    def die(self)
        pass

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.die()
        
