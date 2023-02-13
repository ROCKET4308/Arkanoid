import pygame

class Score:
    def __init__(self, score:int):
        self.score = score

    def increase(self):
        self.score += 1