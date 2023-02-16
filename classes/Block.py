import pygame

class Block:
    """
    A class representing a Block in a Breakout game.

    ...

    Attributes
    ----------
    position : List[int, int]
        A 2-element list representing the position of the Block on the game screen.
    width : int
        The width of the Block.
    height : int
        The height of the Block.
    status : str
        The status of the Block, either "intact" or "destroyed".

    Methods
    -------
    check_collision(ball)
        Checks if the ball has collided with the Block.
    destroy()
        Changes the status of the Block to "destroyed".
    """
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        self.status = "intact"

    def check_collision(self, ball):
        """
        Checks if the ball has collided with the Block.

        Parameters
        ----------
        ball : Ball
            The Ball object that the collision is being checked against.

        Returns
        -------
        bool
            True if the ball has collided with the Block, False otherwise.
        """
        if self.status == "intact":
            if self.position[0] <= ball.position[0] <= self.position[0] + self.width:
                if self.position[1] <= ball.position[1] <= self.position[1] + self.height:
                    return True
        return False

    def destroy(self):
        """
        Changes the status of the Block to "destroyed".
        """
        self.status = "destroyed"