import pygame

class Button:
    def __init__(self, screen, position, size, color, text, onclick):

        self.screen = screen
        self.width_ratio = size[0] / screen.get_width()
        self.height_ratio = size[1] / screen.get_height()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0, 0), size)
        self.onclick = onclick

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def resize(self, screen):
        width = self.width_ratio * screen.get_width()
        height = self.height_ratio * screen.get_height()
        self.image = pygame.transform.scale(self.image, (width, height))
        screen.blit(self.image, self.rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.onclick()

