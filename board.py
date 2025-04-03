import tile

class Board:
    def __init__(self):
        self.array = [
            [],
            [],
            [],
            []
        ]
        self.size = 4 * 10 * 5
        # instantiate the board with tile class
        for i in range(4):
            for j in range(50):
                self.array[i].append(tile.Tile(10, 10))


    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(str(cell) for cell in row) + "\n"
        return board_str

    def move_items(self):
        for i in range(4):
            for j in range(50):
                if self.array[i][j].item is not None:
                    self.array[i][j-1].item = self.array[i][j].item
                    self.array[i][j].item = None
                    