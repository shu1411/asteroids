import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable, )

    # spawn player in the middle of the screen
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    dt = 0

    # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update each player
        updatable.update(dt)

        for ast in asteroids:
            if ast.collides(player):
                print("Game over!")
                sys.exit()
        
        screen.fill("black")

        # draw each player
        for p in drawable:
            p.draw(screen)

        pygame.display.flip()

        # convert from milliseconds to seconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()