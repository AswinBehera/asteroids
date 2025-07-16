import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    Player.containers = (updatable, drawable)
    p1 = Player(x, y)

    g_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        updatable.update(dt)
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
