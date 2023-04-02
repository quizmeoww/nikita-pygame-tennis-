import pygame
import random


class Ball:
    def __init__(self):
        self.image = pygame.image.load('img.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = [random.randint(1, 10), random.randint(1, 10)]

    def respawn(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, 1366)

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        if self.rect.left < 0:
            self.speed[0] = -self.speed[0]
        if self.rect.right > 1366:
            self.speed[0] = -self.speed[0]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
