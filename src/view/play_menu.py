from utils.button import Button
from view.menu import Menu


class PlayMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons.append(Button(screen=screen,
                                   position=(92.5, 2.5),
                                   size=(15, 5),
                                   color=(0, 255, 0),
                                   text='Retour',
                                   font=(100, 60),
                                   onclick=self.go_to_main_menu))

        self.buttons.append(Button(screen=screen,
                                   position=(50, 20),
                                   size=(25, 5),
                                   color=(0, 255, 0),
                                   text='Joueur vs joueur',
                                   font=(130, 100)))

        self.buttons.append(Button(screen=screen,
                                   position=(50, 26),
                                   size=(25, 5),
                                   color=(0, 255, 0),
                                   text='Joueur vs IA',
                                   font=(120, 90)))

    def go_to_main_menu(self):
        from view.main_menu import MainMenu
        MainMenu(self.screen).run()
