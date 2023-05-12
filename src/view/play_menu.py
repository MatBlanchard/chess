from utils.button import Button
from view.menu import Menu


class PlayMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons.append(Button(screen, (650, 0), (150, 50), (0, 255, 0), 'Retour', self.go_to_main_menu))

    def go_to_main_menu(self):
        from view.main_menu import MainMenu
        MainMenu(self.screen).run()
