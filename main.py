import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    Player.containers = (updatable, drawable)
    p1 = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    g_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()

            if asteroid.collide(p1):
                print("Game, Over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = g_clock.tick(60) / 1000

    """"
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    """

if __name__ == "__main__":
    main()
