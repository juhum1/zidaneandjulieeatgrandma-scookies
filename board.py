import tile
import pygame

class Board:
    def __init__(self, cols=4, rows=10, tile_size=80): # col x row 
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.array = [[tile.Tile(tile_size, tile_size) for _ in range(rows)] for _ in range(cols)]
        

    def __str__(self):
        board_str = ""
        for row in self.array:
            board_str += " ".join(str(cell) for cell in row) + "\n"
        return board_str

    def move_items(self):
        for i in range(self.rows - 1, 0, -1):  
            for j in range(self.cols):
                if self.array[i - 1][j].item is not None and self.array[i][j].item is None:
                    self.array[i][j].item = self.array[i - 1][j].item
                    self.array[i - 1][j].item = None



    def draw(self, screen):
        for i, row in enumerate(self.array):
            if i % 5 != 0:  # Only draw every 5th row
                continue
            for j, tile in enumerate(row):
                if j % 5 != 0:  # Only draw every 5th column
                    continue
                if tile.image:
                    screen.blit(tile.image, (j * self.tile_size, i * self.tile_size))