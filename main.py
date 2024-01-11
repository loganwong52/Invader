# python imports
import pygame

# local imports
from player import Player, Tank, Barrel


w = 400
h = 800
halfway = h / 2


# Group single
# player = pygame.sprite.GroupSingle()
# player.add(Player())

tank = pygame.sprite.GroupSingle()
tank.add(Tank())
barrel = pygame.sprite.GroupSingle()
barrel.add(Barrel())


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

        tank.draw(screen)
        tank.update()
        barrel.draw(screen)
        barrel.update()

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
