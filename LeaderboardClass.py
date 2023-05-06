import pygame
import Const
import PlayerClass

class Leaderboard():
	def __init__(self, playerList):
		self.gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.gameScreen.fill(Const.GREY)
		screenWidth, screenHeight = pygame.display.get_surface().get_size()

		self.playerList = playerList

		self.running = True

		self.clock = pygame.time.Clock()

		self.playerContainerWidth = screenWidth / 4

		self.leaderboardText = "LEADERBOARD"
		self.leaderboardTextFont = pygame.font.Font('Assets/Fonts/VCR_OSD_MONO.ttf', 80)
		self.leaderboardTextCoord = ((screenWidth - self.leaderboardTextFont.size(self.leaderboardText)[0]) / 2, 50)
		self.leaderboardTextRender = self.leaderboardTextFont.render(self.leaderboardText, True, Const.WHITE)


	def Run(self):
		while self.running:
			self.clock.tick(10)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.gameScreen.blit(self.leaderboardTextRender, self.leaderboardTextCoord)

			pygame.display.update()