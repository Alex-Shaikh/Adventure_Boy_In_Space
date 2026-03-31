# The main platform class that handles drawing
__author__ = "Alex Shaikh"
__version__ = "3.30.2026"
import pygame
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)

    def draw_me(self, screen,drawColor, camera_y=0):
        draw_rect = self.rect.copy()
        draw_rect.y -= camera_y
        if drawColor != (0,0,0):
            pygame.draw.rect(screen, drawColor, draw_rect)