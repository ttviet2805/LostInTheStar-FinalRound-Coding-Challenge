import pygame
import Const
import CellClass
import PlayerClass
import PlayerStatus
import MapClass
import LeaderboardClass

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
	print(screenWidth, screenHeight)
	running = True

	# Set up Clock
	clock = pygame.time.Clock()
	isEndGame = False

	# Set up Player Status
	statusWidth = (screenWidth - screenHeight) / 2;
	statusHeight = screenHeight * 4 / 10
	statusSize = (statusWidth, statusHeight)
	statusCoord = [(0, screenHeight / 10), (0, screenHeight / 2), (screenWidth - statusWidth, screenHeight / 10), (screenWidth - statusWidth, screenHeight / 2)]
	playerStatusList = []

	statusInfo = (statusCoord, statusSize)

	# Set up step
	step = 0
	isNewStep = False

	# Set up Map
	gameMap = MapClass.Map(gameScreen, screenHeight, statusWidth)
	
	# Set up player
	playerList = []

	# Game Running
	while running :
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
					curScore = gameMap.getScore(cnt)
					i.updateScore(curScore)		
					cnt += 1	

		gameMap.DisplayMap()

		for i in playerList:
			if i != None:
				i.MoveFrame()
				i.drawStatus()

		pygame.display.update()