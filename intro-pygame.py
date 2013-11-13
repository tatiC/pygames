# -*- coding: utf-8 -*-

import pygame

# Defing some colors

black = (0	, 0		,  0)
white = (255, 255, 255)
green = (0	, 255,   0)
red 	= (255,   0,   0)

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
	clock.tick(20)
	
pygame.quit()