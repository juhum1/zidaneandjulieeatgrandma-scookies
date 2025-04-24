from abc import ABC, abstractmethod
import board

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

    def attack_tower(self, tower):
        tower.currentHealth -= self.damage

    def die(self):
        pass

    def take_damage(self, damage: int):
        self.currentHealth -= damage
        # if self.health <= 0:
        #     self.die()


class Goblin(Enemy):
    def __init__(self):
        self.maxHealth = 50 
        self.currentHealth = self.maxHealth
        self.damage = 20
        self.speed = 2 
        self.attackSpeed = 1
        self.attackRange = 1
        self.currency = 10
        self.sprite = "assets/goblin1.png"



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
        self.row = 0
        self.col = 0

    def track_position(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def die(self, board):
        print(f"Witch at ({self.row}, {self.col}) died!")

        board.array[self.row][self.col].item = None
        #board.add_enemy(Skeleton(), self.row, self.col)
        return Skeleton()
