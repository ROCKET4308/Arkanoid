import pygame

class Block:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        self.status = "intact"

