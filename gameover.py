import pygame


w = 400
h = 800
halfway = w / 2
amount = 5


class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        super(Gameover, self).__init__()

        self.image = pygame.Surface((w, 10), pygame.SRCALPHA)
        self.image.fill("black")
        self.rect = self.image.get_rect(midtop=(w / 2, h))

    def update(self):
        pass
