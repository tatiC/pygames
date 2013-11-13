# -*- coding: utf-8 -*-

import pygame
from random import *

# Defing some colors

black = (0	, 0		,  0)
white = (255, 255, 255)
green = (0	, 255,   0)
red 	= (255,   0,   0)
yellow = (243, 250, 55)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tati's cool Game")

done = False
clock = pygame.time.Clock()

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			print "Pressed KEYDOWN babe!"	
	screen.fill(black)	
	pygame.display.flip()
	
	screen = pygame.display.set_mode(size, 0, 32)
	# c_pos = (randint(0, 500), randint(0, 500))   Crazy green ball
	# c_r = randint(10, 100)
	
	# pygame.draw.circle(Surface, color, pos, radius, width=0)
	pygame.draw.circle(screen, yellow, (150,250), 50)
	pygame.draw.circle(screen, red, (550,250), 50)
	pygame.draw.circle(screen, green, (350,250), 50)
	
	pygame.display.flip()
	clock.tick(1)
	
pygame.quit()