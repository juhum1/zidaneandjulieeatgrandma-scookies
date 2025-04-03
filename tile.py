class Tile:
    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        match image:
            case "grass":
                self.image = pygame.image.load("assets/grass.png")
            case _:
                self.image = pygame.image.load("assets/grass.png")


        self.item = None  # Placeholder for item, can be replaced with an actual item class
    

    def __str__(self):
        return f"Tile({self.width}, {self.height}), Image: {self.image}, Item: {self.item})"