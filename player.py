import pygame

class Player:
    def __init__(self):
        self.x = 50
        self.y = 550
        self.width = 40
        self.height = 60
        self.speed = 5

    def move_left(self):
        if self.x - self.speed > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.speed < 800 - self.width:
            self.x += self.speed

    def update(self):
        pass

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if (self.x < obstacle.x + obstacle.width and
                self.x + self.width > obstacle.x and
                self.y < obstacle.y + obstacle.height and
                self.y + self.height > obstacle.y):
                return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 255), (self.x, self.y, self.width, self.height))
