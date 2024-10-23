import pygame

class Window:
    def __init__(self, width, height, name):
        # Window Settings
        self.WINDOW_WIDTH  = width
        self.WINDOW_HEIGHT = height
        self.WINDOW_NAME   = name

        # Defining the Window
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption(self.WINDOW_NAME)