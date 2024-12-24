import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a game clock to control framerate 
    game_clock = pygame.time.Clock()
    dt = 0

    # Create Groups
    updatable = pygame.sprite.Group() # Create container group for all objects to be updated
    drawable = pygame.sprite.Group() # Create group of all objects to be drawn
    asteroids = pygame.sprite.Group() # Create a group of all asteroids
    shots = pygame.sprite.Group() # Create a group of all shots
    
    # Add object classes to Groups
    Player.containers = (updatable, drawable) # add Player class to both groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Instantiate an Asteroid Field Object
    asteroid_field = AsteroidField()
    # Instantiate a player Object
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)


    # Create infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # cleanly shut down pygame
                return
        
        # Update game logic

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                return            
        # Render
        screen.fill("black") # draw screen

        for obj in drawable:
            obj.draw(screen)


        # This MUST happen after ALL other drawing commands
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
   main()
