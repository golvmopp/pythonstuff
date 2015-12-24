import sys, os, math, random
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
        self.enemies = []

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
        bullet.rect.y = self.player.rect.y - 5
        bullet.rect.x = self.player.rect.x + 2
        self.bullets.append(bullet)
        self.fired = 10

    def update_bullets(self):
        for b in self.bullets:
            b.move(UP)
            pygame.draw.rect(self.screen, (255, 255, 255), b.rect)
            if b.rect.bottom < 0:
                self.bullets.remove(b)

    def update_enemies(self):
        if len(self.enemies) is 0:
            new_enemy = Enemy((300, 0)) # Make something random
            self.enemies.append(new_enemy)

        for e in self.enemies:
            e.move()
            pygame.draw.rect(self.screen, (255, 255, 255), e.rect)
            if e.rect.top > 900:
                self.enemies.remove(e)

    def collisions(self):
        for b in self.bullets:
            if b.rect.colliderect(self.player.rect):
                self.player.health -= b.damage
                if self.player.health <= 0:
                    self.game_over()
            for e in self.enemies:
                if b.rect.colliderect(e.rect):
                    e.health -= b.damage
                    if e.health <= 0:
                        self.enemies.remove(e)
                    self.bullets.remove(b)

    def game_over(self):
        font = pygame.font.Font(None, 100)
        text = font.render("YOU LOST", 1, (255, 0, 0))
        textpos = text.get_rect(centerx=325, centery=200)
        self.screen.blit(text, textpos)

        pygame.display.flip()

        while 1:
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                sys.exit()



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

            self.update_enemies()
            self.process_input()
            self.update_bullets()
            self.collisions()

            pygame.draw.rect(self.screen, (255, 255, 255), self.player.rect)
            pygame.display.flip()

RIGHT = DOWN = 1
LEFT = UP = -1

if __name__ == "__main__":
    Main().game()