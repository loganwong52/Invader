# python imports
import pygame


w = 720
h = 1280
halfway = h / 2


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

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
