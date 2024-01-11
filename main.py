# python imports
import pygame
from random import randint

# local imports
from player import Tank, Barrel
from bullet import Bullet
from enemy import Enemy
from gameover import Gameover

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
gameover_sprite = pygame.sprite.GroupSingle()
gameover_sprite.add(Gameover())

# Group
enemy_group = pygame.sprite.Group()
enemy_group.add(Enemy(w / 2, h / 2))


def collision_sprite():
    """
    player is a GroupSingle that is NOT a sprite
    pass in sprite that collides
    pass in Group of sprites that can be collided into
    pass in if the enemy should be deleted or not

    returns 1 to increment the score, or 0 if not
    """
    global bullet, enemy_group

    collided_enemy = pygame.sprite.spritecollideany(bullet.sprite, enemy_group)
    if collided_enemy != None:
        collided_enemy.kill()
        bullet.empty()
        return 1
    return 0


def check_gameover():
    """
    Checks if an enemy has hit the bottom or not.
    """
    global enemy_group, gameover_sprite

    if pygame.sprite.spritecollide(gameover_sprite.sprite, enemy_group, True):
        print("game over!")
        return False
    return True


def main():
    pygame.init()
    # CREATE DISPLAY SURFACE
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Space Invaders")

    # Create the clock object for the framerate
    clock = pygame.time.Clock()

    # Create bullet status helpers
    bullet_ready = True
    bullet_status = "Flying"
    # Timer for bullet
    bullet_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(bullet_timer, 1100)

    # Score
    score = 0
    font = pygame.font.Font("freesansbold.ttf", 25)

    # Timer for enemies
    enemy_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(enemy_timer, 1000)

    game_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
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
            else:
                # Space bar resets the game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    score = 0
                    enemy_group.empty()
                    bullet.empty()
                    game_active = True

        if game_active:
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

            gameover_sprite.draw(screen)
            gameover_sprite.update()

            if bullet.sprite is not None and enemy_group is not None:
                score += collision_sprite()

            # Show instructions if score is 0, otherwise show the score
            score_msg = font.render(f"Score: {score}", False, "White")
            score_msg_rect = score_msg.get_rect(topright=(w, 0))
            screen.blit(score_msg, score_msg_rect)

            if enemy_group is not None:
                game_active = check_gameover()
        else:
            # You've lost
            screen.fill("red")
            # Show final score
            score_msg = font.render(f"Final Score: {score}", False, "Black")
            score_msg_rect = score_msg.get_rect(center=(w / 2, h / 2))
            # press space to start a new game
            restart_msg = font.render("Press Enter to restart!", False, "Black")
            restart_msg_rect = restart_msg.get_rect(center=(w / 2, h / 2 + 50))

            screen.blit(score_msg, score_msg_rect)
            screen.blit(restart_msg, restart_msg_rect)

        # Update everything
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
