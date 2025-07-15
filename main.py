import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    p1 = Player(x, y)

    g_clock = pygame.time.Clock()
    dt = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        p1.draw(screen)
        pygame.display.flip()

        dt = g_clock.tick(60) / 1000

    """"
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    """

if __name__ == "__main__":
    main()
