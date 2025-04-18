import tile
import pygame
import towers
import enemies

class Board:
    def __init__(self, cols, rows, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.array = [[tile.Tile(tile_size, tile_size) for _ in range(cols)] for _ in range(rows)]
        self.player_health = 1000

    def __str__(self):
        board_str = ""
        for row in self.array:
            board_str += " ".join(str(cell) for cell in row) + "\n"
        return board_str
   
    def clear_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.array[i][j].item = None 

    def add_enemy(self, enemy, col):
        if col < self.cols and self.array[0][col].item is None:
            self.array[0][col].item = enemy

    def move_enemies(self):
        damage = 0
        for i in range(self.rows - 1, -1, -1):
            for j in range(self.cols):
                enemy = self.array[i][j].item
                if enemy is not None and isinstance(enemy, enemies.Enemy):
                    if enemy.currentHealth <= 0:
                        self.array[i][j].item = None
                        enemy.die()
                    else:
                        next_row = i + 1
                        if next_row >= self.rows:
                           # print("Enemy reached end!")
                            self.array[i][j].item = None
                            damage += enemy.damage
                        elif self.array[next_row][j].item is None:
                            self.array[next_row][j].item = enemy
                            self.array[i][j].item = None
                        elif isinstance(self.array[next_row][j].item, towers.Tower):
                            enemy.attack_tower(self.array[next_row][j].item)
                        elif isinstance(self.array[next_row][j].item, enemies.Enemy):
                            pass  
        return damage       

    def wave_cleared(self, num_enemies, spawn_rate, time_passed):
        if time_passed > num_enemies * spawn_rate: 
            for i in range(self.rows - 1, -1, -1):
                for j in range(self.cols):
                    enemy = self.array[i][j].item
                    if enemy is not None and isinstance(enemy, enemies.Enemy):
                        return False
            return True

    def tower_attack(self):
        for i in range(self.rows):
            for j in range(self.cols):
                tower = self.array[i][j].item
                if tower is not None and isinstance(tower, towers.Tower):
                    if tower.currentHealth <= 0:
                        self.array[i][j].item = None  # remove dead tower
                    else:
                        for k in range(i - 1, max(i - tower.range - 1, -1), -1):
                            enemy = self.array[k][j].item
                            if enemy is not None and isinstance(enemy, enemies.Enemy):
                                if enemy.currentHealth > 0:
                                    tower.attack_enemy(enemy)
                                    break  # only attack one enemy



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

