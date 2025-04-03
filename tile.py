class Tile:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = None
        self.item = None  # Placeholder for item, can be replaced with an actual item class
    

    def set_image(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    