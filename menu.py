import pygame
import towers
import enemies

class Menu:
    def __init__(self, screen, x_offset, width, height, currency):
        self.screen = screen
        self.x_offset = x_offset  # The starting x index for the menu
        self.width = width
        self.height = height
        self.currency = currency
        self.tower_options = [
            {"name": "Basic Tower", "price": towers.Classic().price, "image": pygame.image.load(towers.Classic().sprite), "selected": False},
            {"name": "Fast Tower", "price": towers.Fast().price, "image": pygame.image.load(towers.Fast().sprite), "selected": False},
            {"name": "Heavy Tower", "price": towers.Heavy().price, "image": pygame.image.load(towers.Heavy().sprite), "selected": False},

        ]
        self.selected_tower = None
        self.health = 1000  

    def draw(self):
        pygame.draw.rect(self.screen, (100, 100, 100), (self.x_offset, 0, self.width, self.height))  # change to tiles later
        
        # Menu bar
        pygame.draw.rect(self.screen, (200, 200, 200), (self.width - 100, 10, 90, 40))
        font = pygame.font.Font(None, 44)
        self.screen.blit(font.render(("Menu"), True, (255, 255, 255)), (self.width - 96, 14))

        for index, tower in enumerate(self.tower_options):
            y_pos = index // 2 * 160 + 45
            self.screen.blit(tower["image"], (self.x_offset + 20 + (index % 2) * 180, y_pos + 10))  
            font = pygame.font.Font(None, 24)
            text = font.render(f"{tower['name']} - ${tower['price']}", True, (255, 255, 255))
            self.screen.blit(text, (self.x_offset + 40 + (index % 2) * 180, y_pos + 20))
            if tower["selected"]:
                pygame.draw.rect(self.screen, (0, 200, 255), (self.x_offset + 20 + (index % 2) * 180, y_pos, 180, 160), 3)

        # Draw the currency
        font = pygame.font.Font(None, 36)
        currency_text = font.render(f"Currency: ${self.currency}", True, (255, 255, 255))
        self.screen.blit(currency_text, (self.x_offset + 100, y_pos + 450))
        # Draw the health
        health_text = font.render(f"Health: {self.health}", True, (255, 255, 255))
        self.screen.blit(health_text, (self.x_offset + 100, y_pos + 550))

    def click_menu_bar(self, x_pos, y_pos):
        if self.width - 100 <= x_pos <= self.width - 10 and 10 <= y_pos <= 50:
            pygame.draw.rect(self.screen, (255, 255, 255), (self.width/2 - 100, self.height/2 - 30, 200, 60)) 
            self.screen.blit(pygame.image.load("assets/restart.png"), (self.width/2-27, self.height/2-28))
            return True
        return False
            
    def click_restart_button(self, board, x_pos, y_pos):   # restarts wave
        pygame.draw.rect(self.screen, (0, 0, 0), (self.width/2 - 30, self.height/2 - 30, 64, 64), 3)
        if self.width/2 - 30 <= x_pos <= self.width/2 + 94 and self.height/2 - 30 <= y_pos <= self.height/2 + 94:
            board.clear_board()
            return True
        return False

    def buy_tower(self, x_pos, y_pos):
        for index, tower in enumerate(self.tower_options):
            y = index // 2 * 160 + 85
            x = self.x_offset + 60 + (index % 2) * 180
            if y - 40 <= y_pos <= y + 120 and x - 60 <= x_pos <= x + 140:  # Clicked on a tower
                if self.currency >= tower["price"]:
                    for t in self.tower_options:
                        t["selected"] = False
                        tower["selected"] = True
                    match tower["name"]:
                        case "Basic Tower":
                            self.selected_tower = towers.Classic()
                            print(f"Selected {tower['name']}")
                        case "Fast Tower":
                            self.selected_tower = towers.Fast()
                            print(f"Selected {tower['name']}")
                        case "Heavy Tower":
                            self.selected_tower = towers.Heavy()
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
            self.currency -= self.selected_tower.price
            self.selected_tower = None
            for t in self.tower_options:
                t["selected"] = False
            return True
        return False
    
    def update_currency(self, currency):
        self.currency += currency

    def update_health(self, health):
        self.health -= health
        if self.health <= 0:
            print("Game Over!")
            return False
        return True

    if __name__ == "__main__":
        print("This is a menu module. It should not be run directly.")
