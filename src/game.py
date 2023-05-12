import pygame
from utils.values import *


class Game:
    def __init__(self):
        pass

    # Show methods
    def show_bg(self, surface):
        for row in range(NB_SQUARES):
            for col in range(NB_SQUARES):
                if (row + col) % 2 == 0:
                    color = (234, 233, 210)  # Light blue
                else:
                    color = (75, 115, 153)  # Dark blue
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(surface, color, rect)