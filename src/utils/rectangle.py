import pygame
from PIL import ImageFont


class Rectangle:
    def __init__(self, screen, position, size, color, text=None, font=None):

        # Screen
        self.screen = screen

        # Position
        self.relative_x = position[0]
        self.relative_y = position[1]
        self.relative_position = position

        # Size
        self.relative_width = size[0]
        self.relative_height = size[1]
        self.relative_size = size

        # Color
        self.color = color

        # Text
        self.text = text
        self.font = 'arial.ttf'

        # Font size
        if font:
            self.relative_font_width = font[0]
            self.relative_font_height = font[1]
            self.relative_font_size = font

        self.image = None
        self.rect = None

    @property
    def x(self):
        return self.relative_x * self.screen.get_width() / 100

    @property
    def y(self):
        return self.relative_y * self.screen.get_height() / 100

    @property
    def position(self):
        return self.x, self.y

    @property
    def width(self):
        return self.relative_width * self.screen.get_width() / 100

    @property
    def height(self):
        return self.relative_height * self.screen.get_height() / 100

    @property
    def size(self):
        return self.width, self.height

    @property
    def font_size(self):
        font = ImageFont.truetype(self.font, 100)
        size = font.getsize(self.text)
        width = self.relative_font_width * self.width // size[0]
        height = self.relative_font_height * self.height // size[1]
        return round(min(width, height))

    def draw(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = pygame.Rect((0, 0), self.size)

        if self.text:
            font = pygame.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = self.rect.center

            self.image.blit(text, text_rect)

        # set after centering text
        self.rect.center = self.position

        self.screen.blit(self.image, self.rect)
