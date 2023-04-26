import pygame
import Const

import json

def getMap():
	mapFile = open("Assets/Example.json")

	curMap = []

	mapData = json.load(mapFile)

	curList = mapData['1']['map']['grid']

	m = len(curList)
	n = len(curList[0])

	for i in curList:
		row = []
		for j in i:
			row.append(j)
		curMap.append(row)

	return curMap

def Run():
	gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	pygame.display.set_caption("BombIT")

	pygame.display.flip()

	screenWidth, screenHeight = pygame.display.get_surface().get_size()

	print(screenWidth, screenHeight)

	running = True

	mapList = getMap()

	print(mapList)

	while running :
		gameScreen.fill((100, 100, 100))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		pygame.display.update()