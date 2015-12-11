import sys, os
import pygame
from pygame.locals import *
from classes import *


class Main:
    def __init__(self):
        pygame.init()
        self.width, self.height = 640, 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bullets = []
        self.player = Ship()
        self.fired = 0

    def process_input(self):
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            sys.exit()
        if keys[K_LEFT]:
            self.player.move(LEFT)
        if keys[K_RIGHT]:
            self.player.move(RIGHT)
        if keys[K_UP]:
            self.fire()


    def fire(self):
        if self.fired > 0: 
            return
        bullet = Bullet()
        bullet.rect.y = self.player.rect.y + 5
        bullet.rect.x = self.player.rect.x + 2
        self.bullets.append(bullet)
        self.fired = 10

    def update_bullets(self):
        for b in self.bullets:
            b.move()
            # check for collisions, deal damage
            pygame.draw.rect(self.screen, (255, 255, 255), b.rect)
            if b.rect.bottom < 0:
                self.bullets.remove(b)

    def game(self):
        clock = pygame.time.Clock()

        while 1:
            self.screen.fill((0, 0, 0))
            clock.tick(60)
            if self.fired > 0:
                self.fired -= 1

            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()

            self.process_input()
            self.update_bullets()

            pygame.draw.rect(self.screen, (255, 255, 255), self.player.rect)
            pygame.display.flip()
RIGHT = 1
LEFT = -1
if __name__ == "__main__":
    Main().game()