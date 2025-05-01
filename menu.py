import pygame
import towers
import enemies

class Menu:
    def __init__(self, screen, x_offset, width, height, currency):
        self.screen = screen
        self.x_offset = x_offset 
        self.width = width
        self.height = height
        self.currency = currency
        self.tower_options = [
            {"name": "Basic Tower", "price": towers.Classic.get_price(), "image": pygame.image.load("assets/wizard.png"), "selected": False},
            {"name": "Fast Tower", "price": towers.Fast.get_price(), "image": pygame.image.load(towers.Fast.get_sprite_path()), "selected": False},
            {"name": "Heavy Tower", "price": towers.Heavy.get_price(), "image": pygame.image.load(towers.Heavy.get_sprite_path()), "selected": False},
            {"name": "Princess Tower", "price": towers.Princess.get_price(), "image": pygame.image.load(towers.Princess.get_sprite_path()), "selected": False},
            {"name": "Slowing Tower", "price": towers.Slowing.get_price(), "image": pygame.image.load(towers.Slowing.get_sprite_path()), "selected": False},
            {"name": "Bomb Tower", "price": towers.Bomb.get_price(), "image": pygame.image.load(towers.Bomb.get_sprite_path()), "selected": False}

            ]

        self.selected_tower = None
        self.health = 500  
        self.wave = 0
        self.remove_clicked = False
        self.tower_clicked = None


    def draw(self):
        pygame.draw.rect(self.screen, (100, 100, 100), (self.x_offset, 0, self.width, self.height))  # change to tiles later
        
        # Draw Menu button
        pygame.draw.rect(self.screen, (200, 200, 200), (self.width - 100, 10, 90, 35))
        font = pygame.font.Font(None, 44)
        self.screen.blit(font.render(("Menu"), True, (255, 255, 255)), (self.width - 96, 14))

        for index, tower in enumerate(self.tower_options):
            y_pos = index // 2 * 160 + 45
            self.screen.blit(tower["image"], (self.x_offset + 20 + (index % 2) * 180, y_pos + 10))  
            font = pygame.font.Font(None, 24)
            text = font.render(f"{tower['name']} - ${tower['price']}", True, (255, 255, 255))
            self.screen.blit(text, (self.x_offset + 40 + (index % 2) * 180, y_pos + 20))
            if tower["selected"]:
                pygame.draw.rect(self.screen, (0, 200, 255), (self.x_offset + 20 + (index % 2) * 180, y_pos, 200, 160), 3)
        
        self.screen.blit(pygame.image.load("assets/bomb.png"), (self.x_offset + 350, 625))
        if self.remove_clicked:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x_offset + 350, 625, 60, 60), 4)

        font = pygame.font.Font(None, 36)
        currency_text = font.render(f"Currency: ${self.currency}", True, (255, 255, 255))
        self.screen.blit(currency_text, (self.x_offset + 100, y_pos + 250))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x_offset + 100, y_pos + 290, 200, 20))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x_offset + 100, y_pos + 290, 200 * (self.health / 500), 20))
        font = pygame.font.Font(None, 24)

        # draw wave
        wave_text = font.render(f"Wave: {self.wave}", True, (255, 255, 255))
        self.screen.blit(wave_text, (self.x_offset + 100, y_pos + 320))
        

    def click_menu_bar(self, x_pos, y_pos):
        if self.width - 100 <= x_pos <= self.width - 10 and 10 <= y_pos <= 45:
            for tower in self.tower_options:
                tower["selected"] = False
            pygame.draw.rect(self.screen, (255, 255, 255), (self.width/2 - 100, self.height/2 - 30, 200, 60)) 
            self.screen.blit(pygame.image.load("assets/restart.png"), (self.width/2-27, self.height/2-28))
            self.remove_clicked = False
            return True
        return False
            
    def click_restart_button(self, board, x_pos, y_pos):   # restarts wave
        if self.remove_clicked == True and self.width/2 - 30 <= x_pos <= self.width/2 + 94 and self.height/2 - 30 <= y_pos <= self.height/2 + 94:
            board.clear_board()
            self.health = 500
            self.remove_clicked = False
            for tower in self.tower_options:
                tower["selected"] = False
        
            return True
        return False

    def set_wave(self, wave):
        self.wave = wave

    def buy_tower(self, x_pos, y_pos):
        for index, tower in enumerate(self.tower_options):
            y = index // 2 * 160 + 85
            x = self.x_offset + 60 + (index % 2) * 180
            if y - 40 <= y_pos <= y + 120 and x - 60 <= x_pos <= x + 140:  # Clicked on a tower
                self.remove_clicked = False
                if self.currency >= tower["price"]:
                    for t in self.tower_options:
                        t["selected"] = False
                        tower["selected"] = True
                    match tower["name"]: # match statement to select tower type
                        case "Basic Tower":
                            self.selected_tower = towers.Classic()
                        case "Fast Tower":
                            self.selected_tower = towers.Fast()
                        case "Heavy Tower":
                            self.selected_tower = towers.Heavy()
                        case "Princess Tower":
                            self.selected_tower = towers.Princess()
                        case "Slowing Tower":
                            self.selected_tower = towers.Slowing()
                        case "Bomb Tower":  
                            self.selected_tower = towers.Bomb()

                    return tower

        return None

    def place_tower(self, board, x_pos, y_pos): 
        if not self.selected_tower:
            return False
        col = x_pos // board.tile_size
        row = y_pos // board.tile_size
        if 0 <= col < board.cols and 3 <= row < board.rows and board.array[row][col].item is None:
            board.array[row][col].item = self.selected_tower
            self.currency -= self.selected_tower.price
            self.selected_tower = None
            for t in self.tower_options:
                t["selected"] = False
            return True
            self.remove_clicked = False
        return False

        pygame.draw.rect(self.screen, (255, 255, 255), (self.x_offset + 350, 625, 114, 114), 3)

    def click_remove(self, x_pos, y_pos):
        if self.x_offset + 350 <= x_pos <= self.x_offset + 407 and 625 <= y_pos <= 682:
            self.remove_clicked = not self.remove_clicked
            for tower in self.tower_options:
                tower["selected"] = False
            return True
        return False

    def remove_tower(self, board, x_pos, y_pos): # removes tower if remove_clicked is True
        col = x_pos // board.tile_size
        row = y_pos // board.tile_size
        if 0 <= col < board.cols and 0 <= row < board.rows and isinstance(board.array[row][col].item, towers.Tower):
            return_percent = 50 
            match tower := board.array[row][col].item:
                case towers.Classic():
                    return_currency = (tower.price * return_percent) // 100 
                case towers.Fast():
                    return_currency = (tower.price * return_percent) // 100
                case towers.Heavy():
                    return_currency = (tower.price * return_percent) // 100
                case towers.Princess():
                    return_currency = (tower.price * return_percent) // 100
                case towers.Slowing():
                    return_currency = (tower.price * return_percent) // 100
            board.array[row][col].item = None
            self.update_currency(return_currency)
            self.remove_clicked = False
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

    def quit(self, x_pos, y_pos): # leaves game
        if self.health <= 0 and self.width/2 - 110 <= x_pos <= self.width/2 - 40 and self.height/2 + 30 <= y_pos <= self.height/2 + 60:
            return True
        return False

    def play_again(self, x_pos, y_pos): # in game.py everything resets
        if self.health <= 0 and self.width/2 + 40 <= x_pos <= self.width/2 + 100 and self.height/2 + 30 <= y_pos <= self.height/2 + 60:
            self.health = 500
            return True 
        return False

    def click_tower(self, x_pos, y_pos, board):
        col = x_pos // board.tile_size
        row = y_pos // board.tile_size
        if 0 <= col < board.cols and 0 <= row < board.rows:
            tower = board.array[row][col].item
            if isinstance(tower, towers.Tower):
                self.selected_tower = None
                for t in self.tower_options:
                    t["selected"] = False
                self.remove_clicked = False
                if self.tower_clicked == (row, col):
                    self.tower_clicked = None  # deselect tower if already selected
                else:
                    self.tower_clicked = (row, col)
                
                return True
        self.tower_clicked = None
        return False




    def show_tower_health(self, board, x_pos, y_pos):
        if self.tower_clicked is not None:
            row, col = self.tower_clicked
            if 0 <= col < board.cols and 0 <= row < board.rows:
                tower = board.array[row][col].item
                if isinstance(tower, towers.Tower):
                    health_ratio = tower.currentHealth / tower.maxHealth
                    bar_width = 80
                    bar_height = 10
                    x = col * board.tile_size + (board.tile_size - bar_width) // 2
                    y = row * board.tile_size - bar_height - 5

                    pygame.draw.rect(self.screen, (255, 0, 0), (x, y, bar_width, bar_height))  # red background
                    pygame.draw.rect(self.screen, (0, 255, 0), (x, y, bar_width * health_ratio, bar_height))  # green foreground
    if __name__ == "__main__":
        print("This is a menu module. It should not be run directly.")
