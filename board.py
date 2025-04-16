import tile
import pygame
import towers
import enemies

class Board:
    def __init__(self, cols=4, rows=10, tile_size=80): # col x row 
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.array = [[tile.Tile(tile_size, tile_size) for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        board_str = ""
        for row in self.array:
            board_str += " ".join(str(cell) for cell in row) + "\n"
        return board_str

    def move_enemies(self):
        for i in range(self.rows-1, -1, -1):
            for j in range(self.cols):
                enemy = self.array[i][j].item
                if enemy is not None and isinstance(enemy, enemies.Enemy):
                    if enemy.health <= 0:
                        self.array[i][j].item = None  # Remove dead enemy
                    else:
                        next_row = i + 1
                        if next_row < self.rows and self.array[next_row][j].item is None:  
                            self.array[next_row][j].item = enemy  
                            self.array[i][j].item = None  
                        elif isinstance(self.array[next_row][j].item, towers.Tower):  
                            # enemy doesn't move, attacks tower
                            enemy.attack_tower()

    def death(self):
        currency = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j].item is not None:
                    if isinstance(self.array[i][j].item, enemies.Enemy):
                        if self.array[i][j].item.currentHealth <= 0:
                            currency += self.array[i][j].item.currency 
                            self.array[i][j].item = None
        return currency 

    def add_enemy(self, enemy, col):
        if col < self.cols and self.array[0][col].item is None:
            self.array[0][col].item = enemy

