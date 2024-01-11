# python imports
import pygame

# local imports
from player import Player


w = 400
h = 800
halfway = h / 2


# Group single
player = pygame.sprite.GroupSingle()
player.add(Player())


def main():
    pygame.init()
    # CREATE DISPLAY SURFACE
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Space Invaders")

    # Create the clock object for the framerate
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Game populates
        screen.fill("black")

        player.draw(screen)
        player.update()

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
