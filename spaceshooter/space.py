import sys, os
import pygame
from pygame.locals import *
from classes import *


class Main:

	def __init__(self):
		pygame.init()
		self.width, self.height = 640, 480
		self.screen = pygame.display.set_mode(self.width, self.height)

	def game(self):
		