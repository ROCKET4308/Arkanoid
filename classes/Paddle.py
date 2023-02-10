import pygame

class Paddle:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def move(self, x):
        self.position[0] += x