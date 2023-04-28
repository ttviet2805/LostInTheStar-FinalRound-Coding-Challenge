import pygame
import Const

class Player():
	def __init__(self, gameScreen):
		self.playerFrame = Const.PLAYER_FRAME_DICT
		self.moveDirection = "Down"
		self.curFrame = 0
		self.numFrame = len(self.playerFrame[self.moveDirection])
		self.gameScreen = gameScreen
		self.playerCoord = (5, 5)

	def DisplayFrame(self):
		self.gameScreen.blit(self.playerFrame[self.moveDirection][self.curFrame], self.playerCoord)

	def MoveFrame(self):
		self.HandleEvent()
		self.DisplayFrame()
		self.curFrame = (self.curFrame + 1) % self.numFrame

	def ChangeDirection(self, newDirection):
		if newDirection != "Down" and newDirection != "Up" and newDirection != "Left" and newDirection != "Right":
			return
		if self.moveDirection == newDirection:
			return
		self.moveDirection = newDirection
		self.curFrame = 0
		self.numFrame = len(self.playerFrame[self.moveDirection])

	def HandleEvent(self):
		key = pygame.key.get_pressed()
		# print(key[pygame.K_w])
		if key[pygame.K_UP]:
			self.ChangeDirection("Up")
		if key[pygame.K_DOWN]:
			self.ChangeDirection("Down")
		if key[pygame.K_LEFT]:
			self.ChangeDirection("Left")
		if key[pygame.K_RIGHT]:
			self.ChangeDirection("Right")
