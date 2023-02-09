import pygame

class Ball:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
