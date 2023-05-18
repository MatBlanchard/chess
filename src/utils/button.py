import pygame
from PIL import ImageFont
from utils.rectangle import Rectangle


class Button(Rectangle):
    def __init__(self, screen, position, size, color, text, font, onclick=None):

        # Screen
        super().__init__(screen, position, size, color, text, font)

        # Onclick function
        self.onclick = onclick

        # Cursor
        self.cursor = pygame.SYSTEM_CURSOR_HAND

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if self.onclick:
                    self.onclick()

    def hover(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False


