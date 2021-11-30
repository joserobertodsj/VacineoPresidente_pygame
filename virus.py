import pygame
import random

class Virus(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/virus.png")
        self.image = pygame.transform.scale(self.image, [70, 70])
        self.rect = pygame.Rect(100, 100, 50, 50)
        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)
        self.speed = 1 + random.random () * 2



    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
            



