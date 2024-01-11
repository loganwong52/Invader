import pygame


w = 400
h = 800
halfway = w / 2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()

        self.amount = 20
        self.image = pygame.Surface((20, 30), pygame.SRCALPHA)
        self.image.fill("yellow")
        self.rect = self.image.get_rect(midbottom=(x, y))

    def player_input(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_LEFT]:
        #     # self.direction = "left"
        #     self.rect.x -= self.amount
        #     if self.rect.left <= 20:
        #         self.rect.left = 20

        # if keys[pygame.K_RIGHT]:
        #     # self.direction = "right"
        #     self.rect.x += self.amount
        #     if self.rect.right >= w - 20:
        #         self.rect.right = w - 20

    def destroy(self):
        """
        If the sprite goes off screen, destroy it.
        """
        if self.rect.bottom <= 0:
            self.kill()

    def update(self, game_restart=False):
        self.player_input()

        self.rect.y -= self.amount
