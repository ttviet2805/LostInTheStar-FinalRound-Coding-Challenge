import pygame
import Const
import CellClass
import PlayerClass
import PlayerStatus
import MapClass

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

	# Set up Map
	gameMap = MapClass.Map(gameScreen, screenHeight, statusWidth)

	# Set up Player
	player_1 = PlayerClass.Player(gameScreen, gameMap.GetCell(0, 0))
	player_2 = PlayerClass.Player(gameScreen, gameMap.GetCell(14, 14))

	# Game Running
	while running :
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for i in playerStatusList:
			i.displayStatusImage()

		gameMap.DisplayMap()

		player_1.MoveFrame()
		player_2.MoveFrame()

		pygame.display.update()