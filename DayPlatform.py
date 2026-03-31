# This is a class that inherits platform is a type of platform that controls whether you can see the Night platforms
__author__ = "Alex Shaikh"
__version__ = "3.30.2026"

import pygame
from Platform import Platform
class DayPlatform(Platform):
    def __init__(self, width, height, x, y):
        self.platformType = "day"
        self.color = (237, 232, 95)
        Platform.__init__(self, width, height, x, y)
    # handles all the collisions and teleports the player to the correct position
    def collisions(self,character):
        if self.rect.colliderect(character.rect):
            overlap_right = character.rect.right - self.rect.left  # How far right side penetrates
            overlap_left = self.rect.right - character.rect.left  # How far left side penetrates
            overlap_bottom = character.rect.bottom - self.rect.top  # How far bottom penetrates
            overlap_top = self.rect.bottom - character.rect.top  # How far top penetrates
            fix_overlap = min(overlap_right, overlap_left, overlap_bottom,overlap_top)
            if fix_overlap == overlap_right: # comes from the left
                character.rect.x = self.rect.left - character.rect.width
                return 2
            if fix_overlap == overlap_left: #coming from the right
                character.rect.x = self.rect.right
                return 3
            if fix_overlap == overlap_top: # comes from the bottom
                character.rect.y = self.rect.bottom
                return 4

            if fix_overlap == overlap_bottom: # from on top
                character.rect.y = self.rect.top - character.rect.height +1
                return 6
        return 0 # 0 = no collision
    def update_sprite(self,screen,camera): # draw
        Platform.draw_me(self,screen,self.color,camera)