import pygame
import Const
import PlayerClass

class LeaderboardInfo():
	def __init__(self, gameScreen, containerSize, containerCoord, containerPadding, player, rank):
		self.gameScreen = gameScreen
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()
		self.containerSize = containerSize
		self.containerCoord = containerCoord
		self.containerPadding = containerPadding
		self.containerRect = pygame.Rect(self.containerCoord[0] + self.containerPadding, self.containerCoord[1] + self.containerPadding, self.containerSize[0] - self.containerPadding * 2, self.containerSize[1] - self.containerPadding * 2)
		
		# self.playerInfoCoord = [name, score, rank, rank_image]
		self.rectPadding = 10
		self.rectContent = (self.containerRect.left + self.rectPadding, self.containerRect.top + self.rectPadding, self.containerRect.width - 2 * self.rectPadding, self.containerRect.height - 2 * self.rectPadding)
		
		self.playerInfoCoord = (self.rectContent[0], self.containerRect[1] + self.rectContent[3] * 6 / 10)
		self.player = player
		self.playerInfo = self.player.GetInfo()
		self.playerRank = rank
		self.playerCup = pygame.transform.scale(Const.RANK_CUP[self.playerRank - 1], (60 * self.screenHeight / Const.MSI[1], 60 * self.screenHeight / Const.MSI[1]))

	def Display(self):
		pygame.draw.rect(self.gameScreen, Const.BACKGROUND_COLOR, self.containerRect, border_radius = 15)
		
		infoFont = pygame.font.Font('Assets/Fonts/VCR_OSD_MONO.ttf', 25 * self.screenWidth // Const.MSI[0])

		self.gameScreen.blit(self.playerInfo[3], (self.rectContent[0] + (self.rectContent[2] - self.playerInfo[3].get_width()) / 2, self.rectContent[1] + self.rectContent[3] / 10))

		infoName = infoFont.render("Name: " + self.playerInfo[0], True, Const.PLAYER_COLOR_DICT[self.playerInfo[2]])
		infoNameWidth = infoFont.size("Name: " + self.playerInfo[0])[0]
		self.gameScreen.blit(infoName, (self.playerInfoCoord[0] + (self.rectContent[2] - infoNameWidth) / 2, self.playerInfoCoord[1]))

		infoScore = infoFont.render("Score: " + str(self.playerInfo[1]), True, Const.PLAYER_COLOR_DICT[self.playerInfo[2]])
		infoScoreWidth = infoFont.size("Score: " + str(self.playerInfo[1]))[0]
		self.gameScreen.blit(infoScore, (self.playerInfoCoord[0] + (self.rectContent[2] - infoScoreWidth) / 2, self.playerInfoCoord[1] + 35 * self.screenWidth // Const.MSI[0]))

		infoRank = infoFont.render("Rank: " + str(self.playerRank), True, Const.PLAYER_COLOR_DICT[self.playerInfo[2]])
		infoRankWidth = infoFont.size("Rank: " + str(self.playerRank))[0]
		self.gameScreen.blit(infoRank, (self.playerInfoCoord[0] + (self.rectContent[2] - infoRankWidth) / 2, self.playerInfoCoord[1] + 70 * self.screenWidth // Const.MSI[0]))

		self.gameScreen.blit(self.playerCup, (self.rectContent[0] + (self.rectContent[2] - self.playerCup.get_width()) / 2, self.playerInfoCoord[1] + 120 * self.screenWidth // Const.MSI[0]))


class Leaderboard():
	def __init__(self, playerList):
		# self.gameScreen = pygame.display.set_mode((1280, 720))
		self.gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.background = pygame.transform.scale(pygame.image.load("Assets/Images/Leaderboard/background.jpg"), (pygame.display.get_surface().get_size()))
		self.gameScreen.blit(self.background, (0, 0))
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()

		self.playerList = playerList

		self.running = True

		self.clock = pygame.time.Clock()

		self.leaderboardText = "LEADERBOARD"
		self.leaderboardTextSize = 80 * self.screenWidth // Const.MSI[0]
		print(self.leaderboardTextSize)
		self.leaderboardTextFont = pygame.font.Font('Assets/Fonts/VCR_OSD_MONO.ttf', self.leaderboardTextSize)
		self.leaderboardTextCoord = ((self.screenWidth - self.leaderboardTextFont.size(self.leaderboardText)[0]) / 2, self.screenHeight / 17)
		self.leaderboardTextRender = self.leaderboardTextFont.render(self.leaderboardText, True, Const.WHITE)

		self.playerContainerNum = len(self.playerList)
		
		# sort
		for i in range(self.playerContainerNum):
			for j in range(i + 1, self.playerContainerNum):
				if self.playerList[i].GetInfo()[1] < self.playerList[j].GetInfo()[1]:
					self.playerList[i], self.playerList[j] = self.playerList[j], self.playerList[i]

		self.playerContainerSize = (self.screenWidth / 4, self.screenHeight - (self.leaderboardTextFont.size(self.leaderboardText)[1] + self.screenHeight / 3.5))
		self.playerContainerPadding = self.playerContainerSize[0] / 10

		playerContainerInitCoord = ((self.screenWidth - self.playerContainerSize[0] * self.playerContainerNum) / 2, self.screenHeight - self.playerContainerSize[1] - self.screenHeight / 8.5)
		self.playerContainer = []
		for i in range(self.playerContainerNum):
			playerContainerCoord = ((playerContainerInitCoord[0] + i * self.playerContainerSize[0], playerContainerInitCoord[1]))
			self.playerContainer.append(LeaderboardInfo(self.gameScreen, self.playerContainerSize, playerContainerCoord, self.playerContainerPadding, self.playerList[i], i + 1))

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