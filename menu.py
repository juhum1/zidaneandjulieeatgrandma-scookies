import pygame
import towers
import enemies
class Menu:
    def __init__(self, screen, x_offset, width, height, currency):
        self.screen = screen
        self.x_offset = x_offset  # The starting x position for the menu
        self.width = width
        self.height = height
        self.currency = currency
        self.tower_options = [
            {"name": "Basic Tower", "cost": 100, "image": pygame.image.load("assets/classic.png")},
            {"name": "Fast Tower", "cost": 150, "image": pygame.image.load("assets/tower2.png")},
            
        ]
        self.selected_tower = None

    def draw(self):
        pygame.draw.rect(self.screen, (100, 100, 100), (self.x_offset, 0, self.width, self.height))  # change to tiles later
        
        for index, tower in enumerate(self.tower_options):
            y_pos = index * 120 + 20
            self.screen.blit(tower["image"], (self.x_offset + 20, y_pos))  
            font = pygame.font.Font(None, 24)
            text = font.render(f"{tower['name']} - ${tower['cost']}", True, (255, 255, 255))
            self.screen.blit(text, (self.x_offset + 80, y_pos + 20))

    def buy_tower(self, pos):
        x, y = pos
        if x < self.x_offset:  
            return None
        for index, tower in enumerate(self.tower_options):
            y_pos = index * 120 + 20
            if y_pos <= y <= y_pos + 80:  # Clicked on a tower
                if self.currency >= tower["cost"]:
                    match tower["name"]:
                        case "Basic Tower":
                            self.selected_tower = towers.Classic()
                            print(f"Selected {tower['name']}")
                            return tower
                        case "Fast Tower":
                            self.selected_tower = tower
                            print(f"Selected {tower['name']}")



                    return tower
                else:
                    print("Not enough currency!")
        return None

    def place_tower(self, board, pos):
        if not self.selected_tower:
            return False
        x, y = pos
        col = x // board.tile_size
        row = y // board.tile_size
        if 0 <= col < board.cols and 0 <= row < board.rows and board.array[row][col].item is None:
            board.array[row][col].item = self.selected_tower
            self.currency -= self.selected_tower.price
            self.selected_tower = None
            return True
        return False
