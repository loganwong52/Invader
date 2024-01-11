import pygame


w = 400
h = 800
halfway = w / 2


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super(Tank, self).__init__()

        self.amount = 10
        self.image = pygame.Surface((60, 40), pygame.SRCALPHA)
        self.image.fill("green")
        self.rect = self.image.get_rect(midbottom=(halfway, h))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # self.direction = "left"
            self.rect.x -= self.amount
            if self.rect.left <= 0:
                self.rect.left = 0

        if keys[pygame.K_RIGHT]:
            # self.direction = "right"
            self.rect.x += self.amount
            if self.rect.right >= w:
                self.rect.right = w

    def update(self, game_restart=False):
        self.player_input()

        # if game_restart:
        #     self.rect.midbottom = (halfway, h)


class Barrel(pygame.sprite.Sprite):
    def __init__(self):
        super(Barrel, self).__init__()

        self.amount = 10
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        self.image.fill("green")
        self.rect = self.image.get_rect(midbottom=(halfway, h - 39))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # self.direction = "left"
            self.rect.x -= self.amount
            if self.rect.left <= 20:
                self.rect.left = 20

        if keys[pygame.K_RIGHT]:
            # self.direction = "right"
            self.rect.x += self.amount
            if self.rect.right >= w - 20:
                self.rect.right = w - 20

    def update(self, game_restart=False):
        self.player_input()
