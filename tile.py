import pygame
class Tile: # Grid class for the game board
    def __init__(self, width, height, image="grass"):
        self.width = width
        self.height = height
        self.image = pygame.image.load(f"assets/{image}.png").convert_alpha()
        self.item = None  


    def __str__(self):
        return f"Tile({self.width}, {self.height}), Image: {self.image}, Item: {self.item})"
