import pygame

class Score:
    """
    Class representing a score in the game.

    Attributes:
        score: The current score of the game.
    """
    def __init__(self, score: int):
        """
        The constructor for the Score class.

        Parameters:
            score: The starting score for the game.
        """
        self.score = score

    def increase(self):
        """
        Increases the score by 1.
        """
        self.score += 1