import pygame

class Ball:
    #class variables
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, CONSTS):
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x,self.y), self.RADIUS)

    def update(self):
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
        # TODO:
        # Check if I'm collision (wall position):
            # Flip the velocity
        #Left Wall
        if self.x < (self.CONSTS.BORDER + 15):
            self.vx = -self.vx
        #Top and Bottom Wall
        if self.y < (self.CONSTS.BORDER + 15) or self.y > (self.CONSTS.HEIGHT - 40):
            self.vy = -self.vy
