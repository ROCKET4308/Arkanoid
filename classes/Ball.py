import pygame

class Ball:
    """
       Class representing a ball that can move.

       Attributes:
           position (list): A list of two integers representing the x and y coordinates of the ball's position.
           speed (list): A list of two integers representing the x and y speed of the ball.

       Methods:
           move: Updates the position of the ball by adding the speed to the current position.
    """
    def __init__(self, position:List[int], speed:List[int]):
        """
           The constructor for the Ball class.

           Parameters:
                    position (list): A list of two integers representing the x and y coordinates of the ball's position.
                    speed (list): A list of two integers representing the x and y speed of the ball.
        """
        self.position = position
        self.speed = speed

    def move(self):
        """
            Updates the position of the ball by adding the speed to the current position.
        """
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
