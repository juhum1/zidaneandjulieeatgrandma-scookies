import tile
import pygame
import towers
import enemies
import projectile

class Board:
    def __init__(self, cols, rows, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.array = [[tile.Tile(tile_size, tile_size) for _ in range(cols)] for _ in range(rows)]
        self.player_health = 500
        self.projectiles = []

    def __str__(self):
        board_str = ""
        for row in self.array:
            board_str += " ".join(str(cell) for cell in row) + "\n"
        return board_str
   
    def clear_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.array[i][j].item = None 

    def add_enemy(self, enemy, row, col):
        if col < self.cols and self.array[row][col].item is None:
            enemy.row = row
            enemy.col = col
            self.array[row][col].item = enemy

    def move_enemies(self, board):
        damage = 0
        for i in range(self.rows - 1, -1, -1):
            for j in range(self.cols):
                enemy = self.array[i][j].item
                if enemy is not None and isinstance(enemy, enemies.Enemy):
                    next_row = i + 1
                    if next_row >= self.rows:
                        self.array[i][j].item = None
                        damage += enemy.damage
                    elif self.array[next_row][j].item is None:
                        self.array[next_row][j].item = enemy
                        self.array[i][j].item = None
                        enemy.row = next_row
                        enemy.col = j
                    elif (next_row + enemy.attackRange - 1) < self.rows:
                        if isinstance(self.array[next_row + enemy.attackRange - 1][j].item, towers.Tower):
                            enemy.attack_tower(self.array[next_row + enemy.attackRange - 1][j].item)
                    elif isinstance(self.array[next_row][j].item, enemies.Enemy):
                        pass  
        return damage       

    def wave_over(self, num_enemies, spawn_rate, time_passed):
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
                        self.array[i][j].item = None
                    else:
                        for k in range(i - 1, max(i - tower.range - 1, -1), -1):
                            enemy = self.array[k][j].item
                            if enemy is not None and isinstance(enemy, enemies.Enemy):
                                if enemy.currentHealth > 0:
                                    new_projectile = projectile.Projectile(
                                        start_pos = (j * self.tile_size, i * self.tile_size), 
                                        target = enemy,
                                        damage = tower.damage,
                                        range = tower.range,
                                        target_y = k * self.tile_size  # enemy's row → Y
                                    )
                                    self.projectiles.append(new_projectile)
                                    tower.shoot(enemy, self, i, j, k)
                                    break


    def death(self):
        currency = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j].item is not None:
                    if isinstance(self.array[i][j].item, enemies.Enemy):
                        if self.array[i][j].item.currentHealth <= 0:
                            currency += self.array[i][j].item.currency
                            item = self.array[i][j].item
                            result = item.die(self)
                            if isinstance(result, list):
                                self.array[i][j].item = None
                                row = i 
                                col = j
                                for enemy in result:    
                                    self.add_enemy(enemy, i, j)
                                    i -= 1
                            else:
                                self.array[i][j].item = result 
                            

        return currency 

