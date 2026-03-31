# A class that inherits platform and can only be seen when on a day platform
__author__ = "Alex Shaikh"
__version__ = "3.30.2026"
import pygame
from Platform import Platform
class NightPlatform(Platform):
    def __init__(self, width, height, x, y):
        self.platformType = "night"
        self.color = (117, 40, 161)
        self.offColor = (0,0,0)
        Platform.__init__(self, width, height, x, y)
    def collisions(self,character):
        if self.rect.colliderect(character.rect):
            overlap_right = character.rect.right - self.rect.left  # How far right side penetrates
            overlap_left = self.rect.right - character.rect.left  # How far left side penetrates
            overlap_bottom = character.rect.bottom - self.rect.top  # How far bottom penetrates
            overlap_top = self.rect.bottom - character.rect.top  # How far top penetrates
            fix_overlap = min(overlap_right, overlap_left, overlap_bottom,overlap_top)
            if fix_overlap == overlap_right:
                character.rect.x = self.rect.left - character.rect.width
                return 2
            if fix_overlap == overlap_left:
                character.rect.x = self.rect.right
                return 3
            if fix_overlap == overlap_top:
                character.rect.y = self.rect.bottom
                return 4
            if fix_overlap == overlap_bottom:
                character.rect.y = self.rect.top - character.rect.height +1
                return 1
        return 0
    def update_sprite(self,screen,camera,on):
        if on:
            Platform.draw_me(self,screen,self.color,camera)
        else:
            Platform.draw_me(self,screen,self.offColor,camera)