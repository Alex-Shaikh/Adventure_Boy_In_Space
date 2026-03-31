# The main player class
__author__ = "Alex Shaikh"
__version__ = "3.30.2026"
import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, min_h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 110))
        self.rect = self.image.get_rect()
        self.rect.y = min_h
        self.rect.x = 400
        self.rect.y = -10300
        frame1 = self.load_and_scale("adventure_boy/sprites/adventBoy_jump.png")
        frame2 = self.load_and_scale("adventure_boy/sprites/adventBoy_stand1.png")
        frame3 = self.load_and_scale("adventure_boy/sprites/adventBoy_stand2.png")
        frame4 = self.load_and_scale("adventure_boy/sprites/adventBoy_walk1.png")
        frame5 = self.load_and_scale("adventure_boy/sprites/adventBoy_walk2.png")
        frame6 = self.load_and_scale("adventure_boy/sprites/adventBoy_walk3.png")
        frame7 = self.load_and_scale("adventure_boy/sprites/adventBoy_walk1 Left.png")
        frame8 = self.load_and_scale("adventure_boy/sprites/adventBoy_walk2 Left.png")
        frame9 = self.load_and_scale("adventure_boy/sprites/adventBoy_walk3 Left.png")
        frame10 = self.load_and_scale("adventure_boy/sprites/adventBoy_jumpRight.png")
        # associated frames for each anim
        self.stand = [frame2, frame3]
        self.jumpLeft = [frame1]
        self.jumpRight = [frame10]
        self.walk = [frame4, frame5, frame6]
        self.walkLeft = [frame7, frame8, frame9]
        self.active = self.walk
        self.time = 0
        self.num = 0
        self.cycle = 0 # how fast animation fram cycle is

    def update(self): # update the sprite animation frame
        self.time += 1
        if self.time > self.cycle:
            self.time = 0
            self.num += 1

        if self.num > len(self.active)-1:
            self.num = 0

        return self.active[self.num]

    def draw(self, screen, height, cameraY): # draw the character
        draw_rect = self.rect.copy()
        draw_rect.y -= cameraY
        if height == 110:
            screen.blit(self.update(), draw_rect)
        else:
            # Adjust for squish
            draw_rect.y -= (height - 110)
            image = pygame.transform.scale(self.update(), (80, height))
            screen.blit(image, draw_rect)

    # Sets the current animation
    def JumpRight(self):
        self.active = self.jumpRight
        self.cycle = 50
    def JumpLeft(self):
        self.active = self.jumpLeft
        self.cycle = 50

    def Walk(self):
        self.active = self.walk
        self.cycle = 10
    def WalkLeft(self):
        self.active = self.walkLeft
        self.cycle = 10
    def Stand(self):
        self.active = self.stand
        self.cycle = 20

    def load_and_scale(self, filename): # sets the right size
        """Load an image and scale it down"""
        image = pygame.image.load(filename)
        return pygame.transform.scale(image, (80, 110))