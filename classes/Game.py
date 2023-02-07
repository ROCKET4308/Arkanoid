import pygame

class Game:
    def __init__(self, screen_size):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)


    def run(self):
        running = True
        while running:
            print('run')

        pygame.quit()


