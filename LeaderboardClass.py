import pygame
import Const
import PlayerClass

class LeaderboardInfo():
	def __init__(self, gameScreen, containerSize, containerCoord, containerPadding, player):
		self.gameScreen = gameScreen
		self.containerSize = containerSize
		self.containerCoord = containerCoord
		self.containerPadding = containerPadding
		self.containerRect = pygame.Rect(self.containerCoord[0] + self.containerPadding, self.containerCoord[1] + self.containerPadding, self.containerSize[0] - self.containerPadding * 2, self.containerSize[1] - self.containerPadding * 2)
		
		# self.playerInfoCoord = [name, score, rank, rank_image]
		rectPadding = 10
		self.playerInfoCoord = (self.containerRect.left + rectPadding, self.containerRect.top + self.containerRect.height * 2 / 3 + rectPadding)
		self.player = player


	def Display(self):
		pygame.draw.rect(self.gameScreen, Const.WHITE, self.containerRect, border_radius = 15)
		
		self.player.DisplayInfo(self.gameScreen, self.playerInfoCoord)


class Leaderboard():
	def __init__(self, playerList):
		self.gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.gameScreen.fill(Const.GREY)
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()

		self.playerList = playerList

		self.running = True

		self.clock = pygame.time.Clock()

		self.leaderboardText = "LEADERBOARD"
		self.leaderboardTextFont = pygame.font.Font('Assets/Fonts/VCR_OSD_MONO.ttf', 80)
		self.leaderboardTextCoord = ((self.screenWidth - self.leaderboardTextFont.size(self.leaderboardText)[0]) / 2, 50)
		self.leaderboardTextRender = self.leaderboardTextFont.render(self.leaderboardText, True, Const.WHITE)

		self.playerContainerNum = len(self.playerList)

		self.playerContainerSize = (self.screenWidth / 4, self.screenHeight - (self.leaderboardTextFont.size(self.leaderboardText)[1] + 100))
		self.playerContainerPadding = self.playerContainerSize[0] / 10

		playerContainerInitCoord = ((self.screenWidth - self.playerContainerSize[0] * self.playerContainerNum) / 2, self.screenHeight - self.playerContainerSize[1])
		self.playerContainer = []
		for i in range(self.playerContainerNum):
			playerContainerCoord = ((playerContainerInitCoord[0] + i * self.playerContainerSize[0], playerContainerInitCoord[1]))
			self.playerContainer.append(LeaderboardInfo(self.gameScreen, self.playerContainerSize, playerContainerCoord, self.playerContainerPadding, self.playerList[i]))

	def Run(self):
		while self.running:
			self.clock.tick(10)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.gameScreen.blit(self.leaderboardTextRender, self.leaderboardTextCoord)

			for i in self.playerContainer:
				i.Display()
			pygame.display.update()