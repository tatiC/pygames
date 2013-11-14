# -*- coding: utf-8 -*-

import pygame
from random import *

# Defing some colors

black = (0	, 0		,  0)
blue = (43, 114, 214)
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
	# Crazy green ball
	# c_pos = (randint(0, 500), randint(0, 500))   
	# c_r = randint(10, 100)
	
	# 3 circles
	# pygame.draw.circle(Surface, color, pos, radius, width=0)
	
	# pygame.draw.circle(screen, yellow, (150,250), 50)
	# pygame.draw.circle(screen, red, (550,250), 50)
	# pygame.draw.circle(screen, green, (350,250), 50)
	
	# 3 lines
	# pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
	# pygame.draw.line(window, (255, 255, 255), (0, 0), (30, 50))
	
	# pygame.draw.line(screen, yellow, (0,150), (700, 150), 1)
	# pygame.draw.line(screen, green, (0,200), (700, 200), 3)
	# pygame.draw.line(screen, red, (0,250), (700, 250), 5)
	
	# Drawing a series of lines
	# Draw on the screen several green lines from (0,10) to (100,110) 
	# Next: (0,20) and (100,120)
	
	# for y_offset in range(0,100,30):
	#   	pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
	#   	pygame.draw.line(screen,green,[0,20+y_offset],[200,210+y_offset],5)
	#     	pygame.display.flip()
	#     	clock.tick(1)
	
	# Trying to write my name
	# T
	pygame.draw.line(screen, yellow, (0,100), (100, 100), 1)
	pygame.draw.line(screen, yellow, (50,100), (50, 200), 1)
	
	# A
	pygame.draw.line(screen, green, (150,100), (150, 200), 1)
	pygame.draw.line(screen, green, (150,100), (250, 100), 1)
	pygame.draw.line(screen, green, (250,100), (250, 200), 1)
	pygame.draw.line(screen, green, (150,150), (250, 150), 1)
	
	# T
	pygame.draw.line(screen, red, (300,100), (400, 100), 1)
	pygame.draw.line(screen, red, (350,100), (350, 200), 1)
	
	# I
	pygame.draw.line(screen, blue, (500,100), (500, 200), 1)
	
	
	
	pygame.display.flip()
	clock.tick(1)
	
	
	
	
pygame.quit()