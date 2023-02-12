import pygame
from classes.Ball import Ball
from classes.Paddle import Paddle
from classes.Block import Block
from components.BlocksArray import blocks

class Game:
    def __init__(self, screen_size):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.ball = Ball([450, 400], [2, 2])
        self.paddle = Paddle([450, 450], 80, 20)
        self.blocks = blocks


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
            elif keys[pygame.K_ESCAPE]:
                running = False
            self.update()
            self.render()
            if self.check_game_over():
                running = False
            self.clock.tick(60)
        pygame.quit()

    def update(self):
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


    def render(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (255, 0, 0), self.ball.position, 20)
        pygame.draw.rect(self.screen, (0, 0, 255), (self.paddle.position[0], self.paddle.position[1], self.paddle.width, self.paddle.height))
        for block in self.blocks:
            if block.status == "intact":
                pygame.draw.rect(self.screen, (0, 255, 0),(block.position[0], block.position[1], block.width, block.height))
        pygame.display.update()

    def check_game_over(self):
        if self.ball.position[1] > self.screen.get_height():
            return True
        elif len([block for block in self.blocks if block.status == "intact"]) == 0:
            return True
        return False