import sys, os
import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		# fix sprites and rects and stuff
		self.health = 50
		self.speed = 5
		self.rect = pygame.Rect(300, 850, 15, 15)

	def move(self, dir):
		self.rect.x += self.speed * dir

class Enemy(pygame.sprite.Sprite):
	def __init__(self, spawn_point, health = 10):
		self.health = health
		self.speed = 3
		self.rect = pygame.Rect(spawn_point[0], spawn_point[1], 40, 15)

	def move(self):
		self.rect.y += self.speed

class Bullet(pygame.sprite.Sprite):
	def __init__(self, dmg = 5):
		self.damage = dmg
		self.speed = 6
		self.rect = pygame.Rect(0, 0, 3, 3)

	def move(self, dir):
		self.rect.y += self.speed * dir
