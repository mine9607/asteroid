import pygame

from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a game clock to control framerate 
    game_clock = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # cleanly shut down pygame
                return
        
        # Update game logic


        # Render
        screen.fill("black")
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
   main()
