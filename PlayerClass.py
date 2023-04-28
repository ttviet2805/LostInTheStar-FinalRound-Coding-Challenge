import pygame
import Const
import CellClass

class Player():
	def __init__(self, gameScreen, curCell):
		self.playerFrame = Const.PLAYER_FRAME_LIST
		self.moveDirection = 2
		self.curFrame = 0
		self.numFrame = len(self.playerFrame[self.moveDirection])
		self.gameScreen = gameScreen
		self.playerCell = curCell
		self.playerCoord = self.playerCell.GetCenter()
		self.isMoving = False

	def DisplayFrame(self):
		self.gameScreen.blit(self.playerFrame[self.moveDirection][self.curFrame], self.playerCoord)

	def MoveFrame(self):
		self.HandleEvent()
		self.DisplayFrame()
		self.curFrame = (self.curFrame + 1) % self.numFrame

	def MovePlayer(self):
		newCell = self.playerCell.GetAdj(self.moveDirection)
		self.playerCell = newCell
		self.playerCoord = self.playerCell.GetCenter()

	def ChangeDirection(self, newDirection):
		if self.isMoving or newDirection > 3 or newDirection < 0:
			return
		if self.moveDirection != newDirection:
			self.moveDirection = newDirection
			self.curFrame = 0
			self.numFrame = len(self.playerFrame[self.moveDirection])

		if self.playerCell.GetAdj(self.moveDirection) != None:
			self.MovePlayer() 

	def HandleEvent(self):
		key = pygame.key.get_pressed()
		# print(key[pygame.K_w])
		if key[pygame.K_UP]:
			self.ChangeDirection(0)
		if key[pygame.K_DOWN]:
			self.ChangeDirection(2)
		if key[pygame.K_LEFT]:
			self.ChangeDirection(3)
		if key[pygame.K_RIGHT]:
			self.ChangeDirection(1)
