import pygame


w = 400
h = 800
halfway = w / 2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()

        self.image = pygame.Surface((40, 30))
        self.image.fill("Red")
        self.rect = self.image.get_rect(center=(x, y))
        # self.game_over = False

    def destroy(self):
        """
        If the sprite goes off screen, destroy it.
        """
        if self.rect.bottom >= h:
            self.kill()
            # self.game_over = True

    def update(self):
        self.rect.y += 1

        # self.destroy()
