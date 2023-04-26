import pygame
import Const

# import json

def Run():
	gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	pygame.display.set_caption("BombIT")

	pygame.display.flip()

	screenWidth, screenHeight = pygame.display.get_surface().get_size()

	print(screenWidth, screenHeight)

	running = True

	# f = open("Assets/Example.json")

	while running :
		gameScreen.fill((100, 100, 100))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		pygame.display.update()