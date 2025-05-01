import pygame
import enemies
import towers

class Start_Screen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.clicked = False

    def draw(self, game_board, menu, tile_size):
        if self.clicked == False:
            pygame.draw.rect(self.screen, (32, 35, 54), (0, 0, self.width, self.height))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.width/2 - 50 , self.height/2 + 200, 100, 40))
            font = pygame.font.Font(None, 36)
            self.screen.blit(font.render("START", True, (0, 0, 0)), (self.width/2 - 38, self.height/2 + 208))
        else: 
            for i in range(game_board.rows):
                for j in range(game_board.cols):
                    tile_obj = game_board.array[i][j]
                    self.screen.blit(tile_obj.image, (j * tile_size, i * tile_size))
                    pygame.draw.rect(self.screen, (0, 0, 0), (j * tile_size, i * tile_size, tile_size, tile_size), 1)
                    if isinstance(tile_obj.item, towers.Tower):
                        self.screen.blit(tile_obj.item.sprite_surface, (j * tile_size, i * tile_size))
                    elif isinstance(tile_obj.item, enemies.Enemy):
                        self.screen.blit(pygame.image.load(tile_obj.item.sprite), (j * tile_size, i * tile_size))
            menu.draw()
            return True

    def click_start(self, x_pos, y_pos):
        if (self.width/2 - 49 <= x_pos <= self.width/2 + 99 and self.height/2 + 200 <= y_pos <= self.height/2 + 240):
            self.clicked = True 
        else:
            self.clicked = False
        

