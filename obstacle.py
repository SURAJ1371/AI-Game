import pygame
import random

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 3

    def update(self):
        self.y += self.speed
        if self.y > 600:  # Reset obstacle when off-screen
            self.y = 0
            self.x = random.randint(0, 800)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
