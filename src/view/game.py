from utils.values import *
from utils.board import Board
from utils.button import Button
from view.menu import Menu


class Game(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.board = Board(self.screen, (80, 100), (40, 50), LIGHT_BLUE, DARK_BLUE)
        self.buttons.append(Button(screen=screen,
                                   position=RETURN_BUTTON_POSITION,
                                   size=RETURN_BUTTON_SIZE,
                                   color=(0, 255, 0),
                                   text='Retour',
                                   font=(100, 60),
                                   onclick=self.go_to_play_menu))

    def go_to_play_menu(self):
        from view.play_menu import PlayMenu
        PlayMenu(self.screen).run()

