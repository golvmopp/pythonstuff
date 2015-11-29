"""
To do:
improve countdown
pause menu
exit button in start-menu
options? like speed
split up shit in different files
"""


import os, sys, random, time
import pygame
from pygame.locals import *

BLACK = 0, 0, 0
FPS = 60
WIDTH = 640
HEIGHT = 480
sincepause = 0

class Main:
    def __init__(self, size=(0, 0)):
        pygame.init()
        if size == (0, 0):
            self.size = self.width, self.height = WIDTH, HEIGHT
        else:
            self.size = self.width, self.height = size
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

    def game(self):
        global sincepause
        # object and settings
        self.setup()

        # start menu
        self.start_menu()

        self.countdown()

        # main event loop
        while 1:
            self.clock.tick(FPS)
            if sincepause > 0:
                sincepause -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.process_input()
            self.ball.move()
            self.collisions()
            self.update_screen()
            
    def collisions(self):
        # pong hit
        collide = pygame.sprite.spritecollide(self.ball,
                                                  self.player_sprites,
                                                  False)
        if len(collide) == 1:
            self.ball.x_speed = -self.ball.x_speed
        
        # wall hit
        ballpos = self.ball.rect.topleft
        if ballpos[1] <= 0 or ballpos[1] >= self.height - 24:
            self.ball.y_speed = -self.ball.y_speed

        # goal score
        if ballpos[0] < 0:
            self.player_two.score += 1
            self.ball.set_pos((self.width/2, self.height/2))
            self.countdown()
        if ballpos[0] >= self.width:
            self.player_one.score += 1
            self.ball.set_pos((self.width/2, self.height/2))
            self.countdown()

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render("%s : %s" % 
            (self.player_one.score, self.player_two.score), 1, (255, 0, 0))
        textpos = text.get_rect(centerx=self.width/2)
        self.screen.blit(text, textpos)

        self.ball_sprite.draw(self.screen)
        self.player_sprites.draw(self.screen)
        pygame.display.flip()

    def process_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.player_two.move("UP")
        if keys[K_DOWN]:
            self.player_two.move("DOWN")
        if keys[K_w]:
            self.player_one.move("UP")
        if keys[K_s]:
            self.player_one.move("DOWN")
        if keys[K_ESCAPE]:
            sys.exit()
        if keys[K_f]:
            self.ball.x_speed = -self.ball.x_speed
        if keys[K_SPACE]:
            self.pause()


    def start_menu(self):
        # set up buttons
        self.screen.blit(self.background, (0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render("PLAY", 1, (255, 0, 0))
        textpos = text.get_rect(centerx=self.width/2, centery=150)

        self.screen.blit(text, textpos)

        pygame.display.flip()

        # wait for input
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if textpos.collidepoint(pos):
                    break # continue main loop
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

    def pause(self):
        global sincepause
        # can't pause if just unpaused #fullosning
        if sincepause > 0:
            return
        sincepause = 30

        font = pygame.font.Font(None, 72)
        text = font.render("PAUSED", 1, (255, 255, 255))
        textpos = text.get_rect(centerx=self.width/2, centery=190)

        self.screen.blit(text, textpos)
        pygame.display.flip()

        while 1:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_SPACE:
                    break # end pause

        text.fill(BLACK)
        self.screen.blit(text, textpos)
        pygame.display.flip()

    def setup(self):
        # Load objects and sprites
        self.player_one = Player()
        self.player_two = Player()

        # initial positions (better way?)
        self.player_two.rect.move_ip((self.width - 10, self.height/2))
        self.player_one.rect.move_ip((0, self.height/2))
        
        self.player_sprites = pygame.sprite.Group()
        self.player_sprites.add(self.player_one, self.player_two)

        self.ball = Ball()
        self.ball_sprite = pygame.sprite.RenderPlain(self.ball)

        # set background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((BLACK))

        # repeat keystrokes when held down
        pygame.key.set_repeat(30,30)

    def countdown(self):
        # this function kinda sucks

        font = pygame.font.Font(None, 72)
        text = font.render("3", 1, (255, 255, 255))
        textpos = text.get_rect(centerx=self.width/2, centery=190)

        self.screen.blit(text, textpos)
        pygame.display.flip()

        time.sleep(0.5)

        text.fill(BLACK)
        self.screen.blit(text, textpos)
        pygame.display.flip()

        text = font.render("2", 1, (255, 255, 255))
        self.screen.blit(text, textpos)
        pygame.display.flip()

        time.sleep(0.5)

        text.fill(BLACK)
        self.screen.blit(text, textpos)
        pygame.display.flip()

        text = font.render("1", 1, (255, 255, 255))
        self.screen.blit(text, textpos)
        pygame.display.flip()

        time.sleep(0.5)

        text.fill(BLACK)
        self.screen.blit(text, textpos)
        pygame.display.flip()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spritepath = os.path.join('img', 'player.png')
        self.image = pygame.image.load(self.spritepath).convert()
        self.image = pygame.transform.scale(self.image, (10, 40))
        self.rect = self.image.get_rect()
        self.speed = 4
        self.score = 0

    def move(self, dir):
        ypos = self.rect.topleft[1]
        if dir is "UP" and ypos > 0:
            self.rect.move_ip((0, -self.speed))
        elif dir is "DOWN" and ypos < HEIGHT - 40:
            self.rect.move_ip((0, self.speed))

class Ball(pygame.sprite.Sprite):

    def __init__(self, speed=(5,5)):
        pygame.sprite.Sprite.__init__(self)
        self.spritepath = os.path.join('img', 'ball.png')
        self.image = pygame.image.load(self.spritepath).convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.x_speed, self.y_speed = speed

    def set_pos(self, (x, y)):
        oldpos = self.rect.topleft
        self.move((-oldpos[0], -oldpos[1]))
        self.move((x, y))

    def move(self, dir=(0,0)):
        # Dir is a tuple of x and y movement speed
        if dir == (0, 0):
            self.rect.move_ip(self.x_speed, self.y_speed)
        else:
            self.rect.move_ip(dir[0], dir[1])

if __name__ == '__main__':
    MainWindow = Main()
    MainWindow.game()