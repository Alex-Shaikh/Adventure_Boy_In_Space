import pygame
class Barrel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =self.load_and_scale("adventure_boy/sprites/barrel.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.
    def load_and_scale(self, filename, scale_factor=0.7):
        """Load an image and scale it down"""
        image = pygame.image.load(filename)
        width = int(image.get_width() * scale_factor)
        height = int(image.get_height() * scale_factor)
        return pygame.transform.scale(image, (width, height))
