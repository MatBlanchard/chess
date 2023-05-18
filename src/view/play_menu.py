from view.game import Game
from utils.button import Button
from utils.values import *
from view.menu import Menu


class PlayMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons.append(Button(screen=screen,
                                   position=RETURN_BUTTON_POSITION,
                                   size=RETURN_BUTTON_SIZE,
                                   color=(0, 255, 0),
                                   text='Retour',
                                   font=(100, 60),
                                   onclick=self.go_to_main_menu))

        self.buttons.append(Button(screen=screen,
                                   position=(50, 20),
                                   size=(25, 5),
                                   color=(0, 255, 0),
                                   text='Joueur vs joueur',
                                   font=(130, 100),
                                   onclick=self.show_bg))

        self.buttons.append(Button(screen=screen,
                                   position=(50, 26),
                                   size=(25, 5),
                                   color=(0, 255, 0),
                                   text='Joueur vs IA',
                                   font=(120, 90)))

    def go_to_main_menu(self):
        from view.main_menu import MainMenu
        MainMenu(self.screen).run()

    def show_bg(self):
        Game(self.screen).run()
