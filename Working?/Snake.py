import pygame
from random import randint

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

pygame.display.set_caption('clickey snake')

#Colours 

red = (255, 0, 0)
green = 0, 255, 0)
purple = (255, 0, 255)
black = (0, 0, 0)

#Main Loop

run = True 

while run:

    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.quit
            run = False

pygame.quit()