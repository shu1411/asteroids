import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # spawn player in the middle of the screen
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    dt = 0

    # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update each player
        updatable.update(dt)
        
        screen.fill("black")

        # draw each player
        for p in drawable:
            p.draw(screen)

        pygame.display.flip()

        # convert from milliseconds to seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()