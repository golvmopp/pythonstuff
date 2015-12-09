import sys, os
import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		# fix sprites and rects and stuff
		self.health = 50

class Enemy(pygame.sprite.Sprite):
	def __init__(self, health = 10):
		# fixx sprites and rects and stuff


class Bullet(pygame.sprite.Sprite):
	def __init__(self, dmg = 5):
		# fix sprites and rects and stuff
		self.damage = dmg
