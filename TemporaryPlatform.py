# A class that inherits platform and can only be stood on for a short period of time
__author__ = "Alex Shaikh"
__version__ = "3.30.2026"
import pygame
from Platform import Platform
class TemporaryPlatform(Platform):
    def __init__(self, width, height, x, y):
        self.platformType = "temporary"
        self.color=(160,100,100)
        self.tempColor = (50, 50, 50)
        self.temporaryTime = 0
        self.offTimer = 0
        self.off = False
        Platform.__init__(self, width, height, x, y)
    def collisions(self,character):
        if self.rect.colliderect(character.rect):
            if self.off:
                return 0
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
                self.temporaryTime += 1
                if self.temporaryTime > 105: # whether to despawn the platform
                    self.temporaryTime = 0
                    self.off = True
                    self.offTimer = 220
                    return 0
                character.rect.y = self.rect.top - character.rect.height +1

                return 1

        # print(0)
        self.temporaryTime = 0
        if self.offTimer > 0:
            self.offTimer -= 1
        else:
            self.offTimer = 0
            self.off =False

        return 0

    def update_sprite(self, screen, camera):
        if self.off:
            Platform.draw_me(self, screen,self.tempColor, camera)
        else:
            Platform.draw_me(self, screen,self.color, camera)