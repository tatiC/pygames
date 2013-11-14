# -*- coding: utf-8 -*-

import pygame
from random import *

# Defing some colors

black = (0	, 0		,  0)
blue = (43, 114, 214)
white = (255, 255, 255)
green = (0	, 255,   0)
purple = (206	, 43,   214)
red 	= (255,   0,   0)
yellow = (243, 250, 55)
green_lane = (4, 126, 113)


pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("MY GRID!")

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
	
	point1 = 10
	point2 = 0
	point3 = 500
	point4 = 0
	point5 = 0
	point6 = 700	
	
	
	while point1 < 700:
		pygame.draw.line(screen, yellow, (point1,point2), (point1, point3), 3)
		pygame.draw.line(screen, yellow, (point4,point5), (point6, point5), 3)
		point1 = point1 + 10
		point5 = point5 + 10
		
	pygame.display.flip()
	clock.tick(1)
	
	
	
	
pygame.quit()