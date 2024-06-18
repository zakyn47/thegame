import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.image_index = 0

        for i in range(8):
            img = pygame.image.load(f"images/walk-{i}.png")
            self.images.append(img)
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
            self.facing_right = False
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
            self.facing_right = True
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        #change image every game tick if player moving
        if self.speedx != 0 or self.speedy != 0:
            self.image_index = (self.image_index + 1) % len(self.images)# increment image_index to 7 then reset to 0
            self.image = self.images[self.image_index]#update the current image
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)#flip the image