import pygame
import Const
import CellClass
import PlayerClass
import PlayerStatus
import MapClass
import LeaderboardClass
import MapEngineClass

def CheckMoving(playerList):
	for i in playerList:
		if i != None:
			if i.GetIsMoving():
				return True
	return False

def Run():
	# Init
	pygame.init()

	# Set up Game Window
	gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption("BombIT")
	pygame.display.flip()

	screenWidth, screenHeight = pygame.display.get_surface().get_size()
	gameBackground = pygame.transform.scale(Const.GAME_BACKGROUND, (screenWidth, screenHeight))
	gameScreen.blit(gameBackground, (0, 0))

	running = True

	# Set up Clock
	clock = pygame.time.Clock()
	isEndGame = False

	# Set up Player Status
	statusWidth = screenWidth * 120 / 610;
	statusHeight = screenHeight * 80 / 406
	statusSize = (statusWidth, statusHeight)
	statusCoord = [(0, 0), (screenWidth - statusWidth, 0), (0, screenHeight - statusWidth), (screenWidth - statusWidth, screenHeight - statusHeight)]
	playerStatusList = []

	statusInfo = (statusCoord, statusSize)

	# Set up step
	step = 0
	isNewStep = False

	# Set up Map
	mapHeight = screenHeight * 212/ 406
	mapWidth = mapHeight
	mapCoordX = (screenWidth - mapWidth) / 2
	mapCoordY = screenHeight * 133 / 406
	# print (mapWidth, mapHeight, mapCoordX, mapCoordY)
	gameMap = MapClass.Map(gameScreen, mapWidth, mapHeight, mapCoordX, mapCoordY)
	
	# Set up player
	playerList = []

	# Map engine
	mapEngine = [
		MapEngineClass.MapEngine(gameScreen, (169, 590), (148, 148), 0),
		MapEngineClass.MapEngine(gameScreen, (1231, 590), (148, 148), 1)
	]

	# Game Running
	while running :
		gameScreen.blit(gameBackground, (0, 0))
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Handle event
		key = pygame.key.get_pressed()
		if CheckMoving(playerList) == False and key[pygame.K_RETURN]:
			step += 1
			if str(step) in Const.mapData:
				isNewStep = True
				if step == 1:
					# Set up Player
					for i in range(4):
						if str(i) in Const.mapData[str(step)]["players"]:
							x = Const.mapData[str(step)]["players"][str(i)]["position"]["x"]
							y = Const.mapData[str(step)]["players"][str(i)]["position"]["y"]
							playerList.append(PlayerClass.Player(gameScreen, i, statusInfo, gameMap.GetCell(x, y)))
				else:
					for i in playerList:
						x = Const.mapData[str(step)]["players"][str(i.GetID())]["position"]["x"]
						y = Const.mapData[str(step)]["players"][str(i.GetID())]["position"]["y"]
						i.ChangeCell((x, y))
				# isEndGame = True
			else:
				isEndGame = True

		if isEndGame:
			running = False
			leaderboard = LeaderboardClass.Leaderboard(playerList)
			leaderboard.Run()

		if CheckMoving(playerList) == False and isNewStep:
			isNewStep = False
			gameMap.UpdateMap(step)

			cnt = 0
			for i in playerList:
				if i != None:
					curScore = gameMap.getScore(step, cnt)
					i.updateScore(curScore)		
					isAlive = gameMap.getAlive(step, cnt)
					i.updateAlive(isAlive)
					cnt += 1	

		gameMap.DisplayMap()

		for i in playerList:
			if i != None:
				i.MoveFrame()
				i.drawStatus()

		for i in mapEngine:
			i.MoveFrame()

		pygame.display.update()