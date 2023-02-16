import pygame

class Paddle:
    """
    The Paddle class represents a paddle in a Pong game. It has a position, width and height.
    """
    def __init__(self, position, width, height):
        """
        Initializes a new instance of the Paddle class.

        :param position: A list containing the x and y position of the paddle.
        :param width: The width of the paddle.
        :param height: The height of the paddle.
        """
        self.position = position
        self.width = width
        self.height = height

    def move(self, x):
        """
        Moves the paddle by a certain amount along the x-axis.

        :param x: The distance to move the paddle along the x-axis.
        """
        self.position[0] += x

    def check_collision(self, ball):
        """
        Checks if the ball has collided with the paddle.

        :param ball: An instance of the Ball class.
        :return: A boolean indicating whether a collision has occurred.
        """
        if self.position[0] <= ball.position[0] <= self.position[0] + self.width:
            if self.position[1] <= ball.position[1] <= self.position[1] + self.height:
                return True
        return False