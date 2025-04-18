import pygame
class Tile:
    def __init__(self, width, height, image="grass"):
        self.width = width
        self.height = height
        match image:
            case "grass":
                self.image = pygame.image.load("assets/grass_tile.png")
            case _:
                self.image = pygame.image.load("assets/grass_tile.png")


        self.item = None  
    

    def __str__(self):
        return f"Tile({self.width}, {self.height}), Image: {self.image}, Item: {self.item})"
