import Const
import pygame

class PlayerStatus():
	def __init__(self, gameScreen, playerName, playerColor, statusCoord, statusLen):
		self.gameScreen = gameScreen
		self.playerName = playerName
		self.playerColor = playerColor
		self.statusCoord = statusCoord
		self.statusLen = statusLen
		self.playerScore = 0
		self.statusBackground = pygame.transform.scale(Const.STATUS_BACKGROUND, statusLen)
		
		# Skin
		self.playerSkin = pygame.transform.scale(Const.PLAYER_IMAGE, (statusLen[0] * 5 / 10, statusLen[1] * 6 / 10))
		self.skinCoord = (self.statusCoord[0] + self.statusLen[0] / 10, self.statusCoord[1] + self.statusLen[1] * 1 / 10)
		
		# Player Name
		playerNameFont = pygame.font.Font('Assets/Fonts/AmaticSC-Bold.ttf', 40)
		self.playerNameText = playerNameFont.render(playerName, True, Const.PLAYER_COLOR_DICT[playerColor])
		self.playerNameCoord = (self.statusCoord[0] + self.statusLen[0] * 2 / 10, self.statusCoord[1] + self.statusLen[1] * 7 / 10)

		# Score
		self.playerScoreFont = pygame.font.Font('Assets/Fonts/VCR_OSD_MONO.ttf', 15)
		self.playerScoreText = self.playerScoreFont.render('Score: ' + str(self.playerScore), True, Const.PLAYER_COLOR_DICT[playerColor])
		self.playerScoreCoord = (self.statusCoord[0] + self.statusLen[0] * 6 / 10, self.statusCoord[1] + self.statusLen[1] * 2 / 10)


	def displayStatusImage(self):
		self.gameScreen.blit(self.statusBackground, self.statusCoord)

		self.gameScreen.blit(self.playerSkin, self.skinCoord)

		self.gameScreen.blit(self.playerNameText, self.playerNameCoord)

		self.gameScreen.blit(self.playerScoreText, self.playerScoreCoord)

	def updateScore(self, curScore):
		self.playerScore = curScore
		self.playerScoreText = self.playerScoreFont.render('Score: ' + str(self.playerScore), True, Const.PLAYER_COLOR_DICT[self.playerColor])

	def GetInfo(self):
		return (self.playerName, self.playerScore, self.playerColor)

	