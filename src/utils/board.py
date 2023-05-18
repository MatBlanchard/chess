from utils.values import *
from utils.rectangle import Rectangle


class Board:
    def __init__(self, screen, size, position, ls_color, ds_color):
        self.screen = screen
        self.size = size
        self.position = position
        self.ls_color = ls_color
        self.ds_color = ds_color
        self.squares = self.load_squares()

    def draw(self):
        for square in self.squares:
            square.draw()

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def square_width(self):
        return self.width / NB_SQUARES

    @property
    def square_height(self):
        return self.height / NB_SQUARES

    @property
    def square_size(self):
        return self.square_width, self.square_height

    def load_squares(self):
        result = []
        for row in range(NB_SQUARES):
            for col in range(NB_SQUARES):
                if (row + col) % 2 == 0:
                    color = self.ls_color
                else:
                    color = self.ds_color
                result.append(Rectangle(screen=self.screen,
                                        position=(self.x - self.width/8 * (col-3.5),
                                                  self.y - self.height/8 * (row-3.5)),
                                        size=self.square_size,
                                        color=color))
        return result
