from utils.button import Button
from view.menu import Menu


class MainMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons.append(Button(screen, (275, 150), (250, 50), (0, 255, 0), 'Jouer', self.go_to_play_menu))

    def go_to_play_menu(self):
        from view.play_menu import PlayMenu
        PlayMenu(self.screen).run()






