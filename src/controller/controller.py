from view.main_menu import MainMenu
import pygame
from utils.values import *
from utils.strings import *


class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE), pygame.RESIZABLE)
        pygame.display.set_caption(APP_NAME)

    def run(self):
        MainMenu(self.screen).run()


if __name__ == '__main__':
    Controller().run()
