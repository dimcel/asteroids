import pygame
from constants import *
from player import Player


def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create 2 groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # make the 2 group a playerclass
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # player.update(dt)
        updatable.update(dt)
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        # player.draw(screen)
        pygame.display.flip()

        #limit frames to 60
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
