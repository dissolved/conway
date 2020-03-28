import pygame  # read more about pygame: https://realpython.com/pygame-a-primer/
import time
from life import Life

WINDOW_X = 800
WINDOW_Y = 800
FPS = 3.0


def display_board(life, window):
    # Fill the background with white
    window.fill((255, 255, 255))
    radius = cell_radius(life)
    for x in range(life.size_x):
        for y in range(life.size_y):
            if life.value_at(x, y):
                pygame.draw.circle(window, (0, 0, 255), cell_center(x, y, radius), radius)

    pygame.display.flip()


def cell_radius(life):
    pixels_per_cell = min(WINDOW_X/life.size_x, WINDOW_Y/life.size_y)
    return pixels_per_cell/2


def cell_center(x, y, radius):
    return (2*x*radius + radius, 2*y*radius + radius)


pygame.init()
game = Life()
game.load('tests/game1.txt')


# Set up the drawing window
screen = pygame.display.set_mode([WINDOW_X, WINDOW_Y])


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    display_board(game, screen)
    game.iterate()
    time.sleep(1/FPS)

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    # pygame.display.flip()


# Done! Time to quit.
pygame.quit()
