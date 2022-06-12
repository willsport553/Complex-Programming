# # from platform import java_ver
# from pip import main
# import pygame
# import pygame.freetype
# from pygame.sprite import Sprite
# from pygame.rect import Rect

# BLUE = (106, 159, 181)
# WHITE = (255, 255, 255)

# def create_surface_with_text(text, font_size, text_rgb, bg_rgb): 
#     font = pygame.freetype.SysFont("courier", font_size, bold=True)
#     surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
#     return surface.convert_alpha() 

# class UIElement (Sprite):

#     def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        
#         super().__init__()
        
#         self.mouse_over = False

#         default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)

#         highlighted_image = create_surface_with_text(text, font_size * 1.2, text_rgb, bg_rgb)

#         self.images = [default_image, highlighted_image]
#         self.rects = [
#             default_image.get_rect(center=center_position),
#             highlighted_image.get_rect(center=center_position)]


#     @property
#     def image(self):
#         return self.images[1] if self.mouse_over else self.images[0]
    
#     @property 
#     def rect(self):
#         return self.rects[1] if self.mouse_over else self.rects[0]

#     def update(self, mouse_pos):
#         if self.rect.collidepoint(mouse_pos):
#             self.mouse_over = True
#         else:
#             self.mouse_over = False
        
#     def draw(self, surface): 
#         surface.blit(self.image, self.rect)

#     def main():
#         pygame.innit()

#         screen = pygame.display.set_mode((800,600))

#         uielement = UIElement(
#             center_position=(400, 400),
#             font_size=30, 
#             bg_rgb=BLUE,
#             text_rgb=WHITE,
#             text='Hello World'
#         )

#         while True:
#             for event in pygame.event.get():
#                 pass
#             screen.fill(BLUE)

#             uielement.update(pygame.mouse.get_pos())
#             uielement.draw(screen)
#             pygame.display.flip()

# main() 

import pygame
import sys


# initializing the constructor
pygame.init()

# screen resolution
res = (720,720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255,255,255)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
text = smallfont.render('quit' , True , color)

while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
				pygame.quit()
				
	# fills the screen with a color
	screen.fill((60,25,60))
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
		
	else:
		pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
	
	# superimposing the text onto our button
	screen.blit(text , (width/2+50,height/2))
	
	# updates the frames of the game
	pygame.display.update()







