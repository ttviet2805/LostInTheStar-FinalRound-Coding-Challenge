import pygame
import Const
import CellClass
import PlayerClass

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

	######################################
	# f = open("Assets/Example.json")
	mapList = getMap()
	N = len(mapList)
	cellLen = screenHeight / N
	mapImage = []
	for i in range(0, N):
		row = []
		for j in range(0, N):
			if mapList[i][j] == '0' or mapList[i][j] == '.':
				row.append(CellClass.EmptyCell(gameScreen, (j * cellLen + screenWidth - screenHeight, i * cellLen), cellLen))
			elif mapList[i][j] == '#':
				row.append(CellClass.ObstacleCell(gameScreen, (j * cellLen + screenWidth - screenHeight, i * cellLen), cellLen))
			else:
				row.append(CellClass.DestroyableCell(gameScreen, (j * cellLen + screenWidth - screenHeight, i * cellLen), cellLen))
		mapImage.append(row)
	
	for i in range(0, N):
		for j in range(0, N):
			for dir in range(0, 4):
				ni = i + Const.CELL_MOVE[dir][0]
				nj = j + Const.CELL_MOVE[dir][1]
				if ni < 0 or ni >= N or nj < 0 or nj >= N or isinstance(mapImage[ni][nj], CellClass.ObstacleCell):
					continue
				mapImage[i][j].AddAdj(mapImage[ni][nj], dir)

	######################################
	player_1 = PlayerClass.Player(gameScreen, mapImage[0][2])
	clock = pygame.time.Clock()

	while running :
		clock.tick(10)
		gameScreen.fill((100, 100, 100))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for row in mapImage:
			for cell in row:
				cell.DisplayBackgroundImage()

		player_1.MoveFrame()
		pygame.display.update()