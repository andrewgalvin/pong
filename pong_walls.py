import random
from collections import namedtuple

import pygame
from paddle import Paddle
from ball import Ball

def main():
    pygame.init()
    pygame.display.set_caption('Pong Game')

    WIDTH = 800
    HEIGHT = 400
    BORDER = 20
    VELOCITY = 5
    FPS = 60

    MyConstants = namedtuple("MyConstants", ["WIDTH","HEIGHT","BORDER","VELOCITY","FPS"])

    #vs List: IMMUTABLE
    CONSTS = MyConstants(WIDTH,HEIGHT, BORDER, VELOCITY, FPS)

    #surface
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0,0,0))
    #double buffering: stage updates together; update them at once
    #avoids flickering
    pygame.display.update()

    #Walls
    # Rect(surface, color, rect) -> Rect
    # Rect((left, top), (width, height)) -> Rect
    wcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")
    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH, BORDER)))

    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER, HEIGHT)))

    #bottom wall

    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER)))

    #right wall

    # Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = random.randint(-VELOCITY,VELOCITY)
    # TODO: +/- 45 degree/random

    b0 = Ball(x0,y0, vx0, vy0, screen, wcolor, bgcolor, CONSTS)
    b0.show(wcolor)


    pygame.display.update()
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    # main loop



    while running:
        # event handling, gets all event from the eventqueue
        b0.update()
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        #Ball
        b0.update()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
