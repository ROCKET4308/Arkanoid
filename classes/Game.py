import pygame
from classes.Ball import Ball
from classes.Paddle import Paddle
from classes.Block import Block
from classes.Score import Score
from components.BlocksArray import blocks

class Game:
    """The Game class represents the Breakout game.

        Attributes:
            screen: The screen surface to display the game.
            clock: The clock to control the game's framerate.
            ball: The ball object in the game.
            paddle: The paddle object in the game.
            blocks: A list of block objects in the game.
            score: The score object in the game.

        Methods:
            run: The main loop of the game. It updates and renders the game until the game is over.
            update: Updates the state of the game objects.
            render: Renders the game objects on the screen.
            check_game_over: This method checks if the game is over by checking if the ball has fallen out of the screen or if all blocks have been destroyed.
     """

    def __init__(self, screen_size):
        """The constructor for the Game class.

            Parameters:
                screen_size: The size of the screen to display the game.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.ball = Ball([450, 400], [2, 2])
        self.paddle = Paddle([450, 450], 80, 20)
        self.blocks = blocks
        self.score = Score(0)


    def run(self):
        """The main loop of the game. It updates and renders the game until the game is over."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle.move(-5)
            elif keys[pygame.K_RIGHT]:
                self.paddle.move(5)
            elif keys[pygame.K_ESCAPE]:
                running = False
            self.update()
            self.render()
            if self.check_game_over():
                running = False
            self.clock.tick(60)
        pygame.quit()

    def update(self):
        """Updates the state of the game objects."""
        self.ball.move()
        if self.ball.position[0] <= 0 or self.ball.position[0] >= self.screen.get_width():
            self.ball.speed[0] = -self.ball.speed[0]
        if self.ball.position[1] <= 0:
            self.ball.speed[1] = -self.ball.speed[1]
        if self.paddle.check_collision(self.ball):
            self.ball.speed[1] = -self.ball.speed[1]
        for block in self.blocks:
            if block.check_collision(self.ball):
                block.destroy()
                self.ball.speed[1] = -self.ball.speed[1]
                self.score.increase()


    def render(self):
        """Renders the game objects on the screen."""
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, (255, 255, 255), self.ball.position, 20)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.paddle.position[0], self.paddle.position[1], self.paddle.width, self.paddle.height))
        for block in self.blocks:
            if block.status == "intact":
                pygame.draw.rect(self.screen, (255, 255, 255),(block.position[0], block.position[1], block.width, block.height))
        font = pygame.font.Font(None, 25)
        score_text = font.render("Score: {}".format(self.score.score), True, (255, 255, 255))
        self.screen.blit(score_text, [0, 0])
        pygame.display.update()

    def check_game_over(self):
        """
            This method checks if the game is over by checking if the ball has fallen out of the screen or if all blocks have been destroyed.

            Returns:
                bool: True if the game is over, False otherwise.
        """
        if self.ball.position[1] > self.screen.get_height():
            return True
        elif len([block for block in self.blocks if block.status == "intact"]) == 0:
            return True
        return False