import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    def run(self):
        screen = self.screen
        screen.fill((0, 0, 0))

        running = True
        while running:
            for button in self.buttons:
                button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.WINDOWRESIZED:
                    for button in self.buttons:
                        button.resize(screen)
                for button in self.buttons:
                    button.click(event)
            pygame.display.flip()
