#!/usr/bin/python
# coding: utf-8

# IMPORTS
import time
import pygame
import sys
import os
from pygame.locals import *

# INITS
pygame.init()
pygame.mouse.set_visible(0)

# VARIABLES
x_screen = 450
y_screen = 270

opt = 0
running = 1
x = 0
y = 0
y_slide = 0


# SET SCREEN
fullscreen = pygame.display.set_mode((x_screen,y_screen), RESIZABLE)
fullscreen.fill((165,165,255))	

# FONT
myfont = pygame.font.SysFont("Helvetica", 18)

# SHOW BACKGROUND 		
pygame.draw.rect(fullscreen, (66,66,231), (20,20,x_screen-40,y_screen-40), 0)

#title and credits
title = myfont.render("USB Storage mounted...", 1, (255,255,255))
inst = myfont.render("Create /roms/ folder on USB", 1, (255,255,255))
fullscreen.blit(title, (110, 100))
fullscreen.blit(inst, (110, 130))
pygame.display.flip()
time.sleep(5)


os.system('mount /media/usb0/roms /recalbox/share/roms')
os.system('/bin/bash /etc/init.d/S31emulationstation stop')
os.system('/bin/bash /etc/init.d/S31emulationstation start')
		
pygame.quit()
sys.exit()
	
	



