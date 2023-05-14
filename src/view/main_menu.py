from utils.button import Button
from view.menu import Menu


class MainMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons.append(Button(screen=screen,
                                   position=(50, 20),
                                   size=(25, 5),
                                   color=(0, 255, 0),
                                   text='Jouer',
                                   font=(100, 100),
                                   onclick=self.go_to_play_menu))

    def go_to_play_menu(self):
        from view.play_menu import PlayMenu
        PlayMenu(self.screen).run()






