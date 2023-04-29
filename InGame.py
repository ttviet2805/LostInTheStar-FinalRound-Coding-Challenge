import pygame
import Const
import CellClass
import PlayerClass
import PlayerStatus
import MapClass

def Run():
	gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption("BombIT")
	pygame.display.flip()

	screenWidth, screenHeight = pygame.display.get_surface().get_size()
	print(screenWidth, screenHeight)

	clock = pygame.time.Clock()

	running = True

	# Set up Player Status
	statusWidth = (screenWidth - screenHeight) / 2;
	statusSize = (statusWidth, screenHeight / 2)
	statusCoord = [(0, 0), (0, screenHeight / 2), (screenWidth - statusWidth, 0), (screenWidth - statusWidth, screenHeight / 2)]
	playerStatusList = []

	for i in range(4):
		playerStatusList.append(PlayerStatus.PlayerStatus(gameScreen, "Viet", statusCoord[i], statusSize))


	# Map
	gameMap = MapClass.Map(gameScreen, screenHeight, statusWidth)

	player_1 = PlayerClass.Player(gameScreen, gameMap.GetCell(0, 0))
	player_2 = PlayerClass.Player(gameScreen, gameMap.GetCell(14, 14))

	while running :
		clock.tick(10)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		gameMap.DisplayMap()

		player_1.MoveFrame()
		player_2.MoveFrame()

		for i in playerStatusList:
			i.displayStatusImage()

		pygame.display.update()