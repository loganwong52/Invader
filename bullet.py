import pygame

w = 400
h = 800


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()

        self.amount = 20
        self.image = pygame.Surface((20, 30), pygame.SRCALPHA)
        self.image.fill("yellow")
        self.rect = self.image.get_rect(midbottom=(x, y))

    def destroy(self):
        """
        If the sprite goes off screen, destroy it.
        """
        if self.rect.bottom <= 0:
            self.kill()

    def update(self):
        self.rect.y -= self.amount
