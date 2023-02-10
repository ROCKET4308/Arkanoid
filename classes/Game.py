import pygame
from classes.Ball import Ball
from classes.Paddle import Paddle

class Game:
    def __init__(self, screen_size):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.ball = Ball([100, 100], [2, 2])
        self.paddle = Paddle([500, 500], 80, 20)

    def run(self):
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
            if self.check_game_over():
                running = False


        pygame.quit()

    def check_game_over(self):
        if self.ball.position[1] > self.screen.get_height():
            return True
        return False