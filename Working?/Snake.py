import pygame
from random import randint

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

pygame.display.set_caption('clickey snake')

#Colours 

orange = (255,165,0)
light_blue = (173,216,230)
dark_blue = (0,0,139)
black = (0, 0, 0)

#Redraw Function

def redraw(): 
    win.fill

#Main Loop

run = True 

while run:

    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False

pygame.quit()