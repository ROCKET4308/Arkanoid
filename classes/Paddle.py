import pygame

class Paddle:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def move(self, x):
        self.position[0] += x

    def check_collision(self, ball):
        if self.position[0] <= ball.position[0] <= self.position[0] + self.width:
            if self.position[1] <= ball.position[1] <= self.position[1] + self.height:
                return True
        return False