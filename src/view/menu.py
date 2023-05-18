import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.board = None

    def run(self):
        screen = self.screen
        screen.fill((0, 0, 0))

        while True:
            for button in self.buttons:
                button.draw()
            if self.board:
                self.board.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handle_quit()
                if event.type == pygame.WINDOWSIZECHANGED:
                    self.handle_resize()
                self.handle_buttons(event)

            pygame.display.flip()

    @staticmethod
    def handle_quit():
        pygame.quit()
        exit()

    def handle_resize(self):
        for button in self.buttons:
            button.draw()

    def handle_buttons(self, event):
        hover = False
        hover_button = None
        for button in self.buttons:
            button.click(event)
            if button.hover():
                hover = True
                hover_button = button
            if hover:
                pygame.mouse.set_cursor(hover_button.cursor)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
