import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # make the 2 group a playerclass
    Player.containers = (updatable, drawable)
    # and one asteroid
    Asteroid.containers = (asteroids, updatable, drawable)
    # for shoot objects 
    Shot.containers = (shots, updatable, drawable)



    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        #collision logic
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        # collistion check wiht bullet
            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)


        pygame.display.flip()

        #limit frames to 60
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
