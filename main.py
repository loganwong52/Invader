# python imports
import pygame
from random import randint

# local imports
from player import Tank, Barrel
from bullet import Bullet
from enemy import Enemy

w = 400
h = 800
halfway = h / 2


# Group single
tank = pygame.sprite.GroupSingle()
tank.add(Tank())
barrel = pygame.sprite.GroupSingle()
the_barrel = Barrel()
barrel.add(the_barrel)

bullet = pygame.sprite.GroupSingle()

# Group
enemy_group = pygame.sprite.Group()
enemy_group.add(Enemy(w / 2, h / 2))

# Player score
score = 0


def collision_sprite():
    """
    player is a GroupSingle that is NOT a sprite
    pass in sprite that collides
    pass in Group of sprites that can be collided into
    pass in if the enemy should be deleted or not
    """
    global bullet, enemy_group, score

    collided_enemy = pygame.sprite.spritecollideany(bullet.sprite, enemy_group)
    if collided_enemy != None:
        collided_enemy.kill()
        bullet.empty()
        score += 1
        # return False
    # return True


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
    pygame.time.set_timer(bullet_timer, 1300)

    # Score
    font = pygame.font.Font("freesansbold.ttf", 25)

    # Timer for enemies
    enemy_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_timer, 2500)

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
                    bullet.add(Bullet(the_barrel.rect.x, the_barrel.rect.y))
                    bullet_ready = False

            if event.type == enemy_timer:
                # Spawn a new enemy
                x = randint(40, w - 40)
                y = randint(30, h / 2)
                enemy_group.add(Enemy(x, y))

        # Game populates
        screen.fill("black")

        tank.draw(screen)
        tank.update()
        barrel.draw(screen)
        barrel.update()

        bullet.draw(screen)
        bullet.update()

        enemy_group.draw(screen)
        enemy_group.update()

        if bullet.sprite is not None and enemy_group is not None:
            collision_sprite()

        # Show instructions if score is 0, otherwise show the score
        score_msg = font.render(f"Score: {score}", False, "White")
        score_msg_rect = score_msg.get_rect(topright=(w, 0))
        screen.blit(score_msg, score_msg_rect)

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
