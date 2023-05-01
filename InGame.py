import pygame
import Const
import CellClass
import PlayerClass
import PlayerStatus
import MapClass

import json

def Run():
	# Set up Game Window
	gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption("BombIT")
	pygame.display.flip()

	screenWidth, screenHeight = pygame.display.get_surface().get_size()
	print(screenWidth, screenHeight)
	running = True

	# Set up Clock
	clock = pygame.time.Clock()

	# Set up Player Status
	statusWidth = (screenWidth - screenHeight) / 2;
	statusSize = (statusWidth, screenHeight / 2)
	statusCoord = [(0, 0), (0, screenHeight / 2), (screenWidth - statusWidth, 0), (screenWidth - statusWidth, screenHeight / 2)]
	playerStatusList = []

	for i in range(4):
		playerStatusList.append(PlayerStatus.PlayerStatus(gameScreen, "Viet", statusCoord[i], statusSize))

	# Set up step
	step = 1

	# Set up Map
	gameMap = MapClass.Map(gameScreen, screenHeight, statusWidth)

	# Set up Player
	mapFile = open("Assets/Example.json")
	mapData = json.load(mapFile)
	playerList = []
	for i in range(4):
		if str(i) in mapData[str(step)]["players"]:
			x = mapData[str(step)]["players"][str(i)]["position"]["x"]
			y = mapData[str(step)]["players"][str(i)]["position"]["y"]
			playerList.append(PlayerClass.Player(gameScreen, gameMap.GetCell(x, y)))
		else:
			playerList.append(None)

	# Game Running
	while running :
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Handle event
		key = pygame.key.get_pressed()
		if key[pygame.K_RETURN]:
			step += 1
			if str(step) in mapData:
				for i in range(4):
					if str(i) in mapData[str(step)]["players"]:
						x = mapData[str(step)]["players"][str(i)]["position"]["x"]
						y = mapData[str(step)]["players"][str(i)]["position"]["y"]
						playerList[i].ChangeCell((x, y))


		for i in playerStatusList:
			i.displayStatusImage()

		gameMap.DisplayMap()

		for i in playerList:
			if i != None:
				i.MoveFrame()

		pygame.display.update()