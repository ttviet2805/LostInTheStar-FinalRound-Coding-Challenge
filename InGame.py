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

def CheckAlive(playerList):
	for i in playerList:
		if i != None:
			if i.GetIsAlive():
				return True
	return False

def Run(jsonFile, listTeam):
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
	statusCoord = [(0, 0), (screenWidth - statusWidth, 0), (0, screenHeight - statusHeight), (screenWidth - statusWidth, screenHeight - statusHeight)]
	playerStatusList = []

	statusInfo = (statusCoord, statusSize)

	# Set up step
	step = 0
	curOutsideZone = 0
	isNewStep = False

	# Set up Map
	mapHeight = screenHeight * 212/ 406
	mapWidth = mapHeight
	mapCoordX = (screenWidth - mapWidth) / 2
	mapCoordY = screenHeight * 133 / 406
	# print (mapWidth, mapHeight, mapCoordX, mapCoordY)
	gameMap = MapClass.Map(gameScreen, jsonFile, mapWidth, mapHeight, mapCoordX, mapCoordY)
	
	# Set up player
	playerList = []

	# Set up Map engine
	mapEngineSize = (screenWidth * 62 / 610, screenHeight * 64 / 406)
	MapEngineCoord = (
		(screenWidth * 65 / 610, screenHeight * 278 / 406), 
		(screenWidth * 488 / 610, screenHeight * 278 / 406)
	)
	mapEngine = [
		MapEngineClass.MapEngine(gameScreen, MapEngineCoord[0], mapEngineSize, 0),
		MapEngineClass.MapEngine(gameScreen, MapEngineCoord[1], mapEngineSize, 1)
	]

	print(listTeam)

	pregameImage = pygame.transform.scale(Const.PREGAME_BACKGROUND, (screenWidth, screenHeight))
	
	while(True):
		tick = pygame.time.get_ticks()
		print(tick)
		if(tick >= 8000): 
			break
		gameScreen.blit(pregameImage, (0, 0))
		pygame.display.update()
	
	pygame.mixer.Sound.play(Const.INGAME_SOUND, loops = -1)

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
			if str(step) in MapClass.getMapData(jsonFile):
				isNewStep = True
				frequency = MapClass.getMapData(jsonFile)[str(step)]["frequency"]
				if step == 1:
					# Set up Player
					for i in range(4):
						if str(i) in MapClass.getMapData(jsonFile)[str(step)]["players"]:
							x = MapClass.getMapData(jsonFile)[str(step)]["players"][str(i)]["position"]["x"]
							y = MapClass.getMapData(jsonFile)[str(step)]["players"][str(i)]["position"]["y"]
							playerList.append(PlayerClass.Player(gameScreen, i, listTeam[i], statusInfo, gameMap.GetCell(x, y)))
					for i in playerList:
						i.UpdateCoord()
				else:
					for i in playerList:
						x = MapClass.getMapData(jsonFile)[str(step)]["players"][str(i.GetID())]["position"]["x"]
						y = MapClass.getMapData(jsonFile)[str(step)]["players"][str(i.GetID())]["position"]["y"]
						i.ChangeCell((x, y))
				if CheckAlive(playerList):
					if (step - 1) % frequency == 0:
						curOutsideZone = (step - 1) / frequency
				else:
					curOutsideZone += 1
				# isEndGame = True
			else:
				isEndGame = True

		if isEndGame:
			running = False
			pygame.mixer.stop()
			leaderboard = LeaderboardClass.Leaderboard(playerList)
			leaderboard.Run()
			break

		if CheckMoving(playerList) == False and isNewStep:
			isNewStep = False
			gameMap.UpdateMap(step, curOutsideZone)

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