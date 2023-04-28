import pygame
import Const
import CellClass
import PlayerClass
import PlayerStatus

import json

def getMap(step):
	mapFile = open("Assets/Example.json")

	curMap = []

	mapData = json.load(mapFile)

	curList = mapData[str(step)]['map']['grid']

	m = mapData[str(step)]['map']['rows']
	n = mapData[str(step)]['map']['columns']

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

	# Set up Player Status
	statusWidth = (screenWidth - screenHeight) / 2;
	statusSize = (statusWidth, screenHeight / 2)
	statusCoord = [(0, 0), (0, screenHeight / 2), (screenWidth - statusWidth, 0), (screenWidth - statusWidth, screenHeight / 2)]
	playerStatusList = []

	for i in range(4):
		playerStatusList.append(PlayerStatus.PlayerStatus(gameScreen, "Viet", statusCoord[i], statusSize))


	###########################################
	mapList = getMap(0)
	N = len(mapList)
	cellLen = screenHeight / N
	mapImage = []

	for i in range(0, N):
		row = []
		for j in range(0, N):
			if mapList[i][j] == '0' or mapList[i][j] == '.':
				row.append(CellClass.EmptyCell(gameScreen, (j * cellLen + statusWidth, i * cellLen), cellLen))
			elif mapList[i][j] == '#':
				row.append(CellClass.ObstacleCell(gameScreen, (j * cellLen + statusWidth, i * cellLen), cellLen))
			else:
				row.append(CellClass.DestroyableCell(gameScreen, (j * cellLen + statusWidth, i * cellLen), cellLen))
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
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for row in mapImage:
			for cell in row:
				cell.DisplayBackgroundImage()

		player_1.MoveFrame()

		for i in playerStatusList:
			i.displayStatusImage()

		pygame.display.update()