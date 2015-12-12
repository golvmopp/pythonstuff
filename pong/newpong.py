import sys
import pygame
import math
from pygame.locals import *


class Main(object):
    """The main class with almost everything in it"""
    def __init__(self):
        super(Main, self).__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.ball = pygame.Rect(400, 300, 5, 5)
        self.ballDir = math.radians(0)
        self.ballSpeed = 10

        self.playerRects = {
            -60:pygame.Rect(50, 380, 10, 20), # Bottom of paddle
            -45:pygame.Rect(50, 360, 10, 20),
            -30:pygame.Rect(50, 340, 10, 20),
            -0:pygame.Rect(50, 320, 10, 20),
            30:pygame.Rect(50, 300, 10, 20),
            45:pygame.Rect(50, 280, 10, 20),
            60:pygame.Rect(50, 260, 10, 20), # Top of paddle
        }

    def draw_players(self):
        for r in self.playerRects:
            pygame.draw.rect(self.screen, (255, 255, 255), self.playerRects[r])

    def update_player(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if self.playerRects[60].y > 0:
                for r in self.playerRects:
                    self.playerRects[r].y -= 5 # speed
        if keys[K_DOWN]:
            if self.playerRects[-60].y < 580:
                for r in self.playerRects:
                    self.playerRects[r].y += 5 # speed            

    def update_ball(self):
        if self.ball.y <= 0 or self.ball.y > 595:
            self.ballDir *= -1



    def run(self):
        clock = pygame.time.Clock()

        while 1:
            self.screen.fill((0, 0, 0))
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

            self.update_ball()
            pygame.draw.rect(self.screen, (255, 255, 255), self.ball)

            self.update_player()
            self.draw_players()
            pygame.display.flip()




if __name__ == "__main__":
    g = Main()
    g.run()