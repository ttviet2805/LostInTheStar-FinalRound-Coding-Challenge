import Const
import pygame

class PlayerStatus():
	def __init__(self, gameScreen, playerName, statusCoord, statusLen):
		self.gameScreen = gameScreen
		self.playerName = playerName
		self.statusCoord = statusCoord
		self.statusLen = statusLen
		self.statusBackground = pygame.transform.scale(Const.STATUS_BACKGROUND, statusLen)
		# self.playerSkin = pygame.transform.scale(Const.PLAYER_IMAGE, (statusLen[0] - 40, statusLen[1] - 40))

	def displayStatusImage(self):
		self.gameScreen.blit(self.statusBackground, self.statusCoord)
		# self.gameScreen.blit(self.playerSkin, self.statusCoord)



