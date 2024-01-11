import pygame


w = 400
h = 800
halfway = w / 2


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()

        self.amount = 20
        self.image = pygame.Surface((20, 30), pygame.SRCALPHA)
        self.image.fill("yellow")
        self.rect = self.image.get_rect(midbottom=(halfway, h))

    def player_input(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_SPACE]:
        # print("bullet fired")

    def destroy(self):
        """
        If the sprite goes off screen, destroy it.
        """
        if self.rect.bottom <= 0:
            self.kill()

    def update(self, game_restart=False):
        self.player_input()

        self.rect.y -= self.amount
