# python imports
import pygame

# local imports
from player import Tank, Barrel
from bullet import Bullet

w = 400
h = 800
halfway = h / 2


# Group single
tank = pygame.sprite.GroupSingle()
tank.add(Tank())
barrel = pygame.sprite.GroupSingle()
barrel.add(Barrel())

bullet = pygame.sprite.GroupSingle()


def main():
    pygame.init()
    # CREATE DISPLAY SURFACE
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Space Invaders")

    # Create the clock object for the framerate
    clock = pygame.time.Clock()

    bullet_ready = True
    bullet_status = "Flying"
    # Timer for bullet
    bullet_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(bullet_timer, 1500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == bullet_timer:
                if not bullet_ready:
                    bullet_ready = True
                    bullet_status = "Flying"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print(bullet_status)
                if bullet_ready:
                    bullet_status = "cooldown"
                    bullet.add(Bullet())
                    bullet_ready = False

        # Game populates
        screen.fill("black")

        tank.draw(screen)
        tank.update()
        barrel.draw(screen)
        barrel.update()

        bullet.draw(screen)
        bullet.update()

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
