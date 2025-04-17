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
            {"name": "Basic Tower", "cost": towers.Classic().price, "image": pygame.image.load(towers.Classic().sprite)},
            {"name": "Fast Tower", "cost": towers.Fast().price, "image": pygame.image.load(towers.Fast().sprite)},
            
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

        # Draw the currency
        font = pygame.font.Font(None, 36)
        currency_text = font.render(f"Currency: ${self.currency}", True, (255, 255, 255))
        self.screen.blit(currency_text, (self.x_offset + 100, y_pos + 600))

    def buy_tower(self, x_pos, y_pos):
        if x_pos < self.x_offset:  
            return None
        for index, tower in enumerate(self.tower_options):
            y = index * 120 + 20
            if y <= y_pos <= y + 80:  # Clicked on a tower
                if self.currency >= tower["cost"]:
                    match tower["name"]:
                        case "Basic Tower":
                            self.selected_tower = tower
                            print(f"Selected {tower['name']}")
                        case "Fast Tower":
                            self.selected_tower = tower  
                            print(f"Selected {tower['name']}")

                    return tower
                else:
                    print("Not enough currency!")
        return None

    def place_tower(self, board, x_pos, y_pos):
        if not self.selected_tower:
            return False
        col = x_pos // board.tile_size
        row = y_pos // board.tile_size
        if 0 <= col < board.cols and 0 <= row < board.rows and board.array[row][col].item is None:
            board.array[row][col].item = self.selected_tower
            self.currency -= self.selected_tower["cost"]
            self.selected_tower = None
            return True
        return False
    
    def update_currency(self, currency):
        self.currency += currency
