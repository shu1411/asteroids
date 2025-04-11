import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # spawn player in the middle of the screen
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        # convert from milliseconds to seconds
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()