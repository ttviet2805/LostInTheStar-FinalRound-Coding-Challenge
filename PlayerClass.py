import pygame
import Const
import CellClass

class Player():
	def __init__(self, gameScreen, curCell):
		self.gameScreen = gameScreen
		self.playerCell = curCell
		self.playerCoord = self.playerCell.GetCenter()
		self.playerFrameHeight = self.playerCell.GetLen() / 5 * 4
		self.playerFrameWidth = self.playerFrameHeight / 7 * 5
		self.playerPadding = ((self.playerCell.GetLen() - self.playerFrameWidth) / 2, (self.playerCell.GetLen() - self.playerFrameHeight) / 2) 

		self.playerFrame = []
		for listFrame in Const.PLAYER_FRAME_LIST:
			playerFrameList = []
			for frame in listFrame:
				playerFrameList.append(pygame.transform.scale(frame, (self.playerFrameWidth, self.playerFrameHeight)))
			self.playerFrame.append(playerFrameList)

		self.moveDirection = 2
		self.curFrame = 0
		self.numFrame = len(self.playerFrame[self.moveDirection])
		self.isMoving = False
		self.moveSpeed = 8
		self.instructionPath = "Assets/Instructions/Player1.txt"
		self.instructionFile = open(self.instructionPath, 'r')

	def DisplayFrame(self):
		self.gameScreen.blit(self.playerFrame[self.moveDirection][self.curFrame], (self.playerCoord[0] + self.playerPadding[0], self.playerCoord[1] + self.playerPadding[1]))

	def GetIsMoving(self):
		return self.isMoving

	def MoveFrame(self):
		if self.isMoving:
			self.MovePlayer()
		self.DisplayFrame()
		self.curFrame = (self.curFrame + 1) % self.numFrame

	def MovePlayer(self):
		newCell = self.playerCell.GetAdj(self.moveDirection)
		if self.playerCoord == newCell.GetCenter():
			self.playerCell = newCell
			self.playerCoord = self.playerCell.GetCenter()
			self.isMoving = False
			return
		newCoord = []
		for i in range(0, 2):
			moveLen = min(abs(newCell.GetCenter()[i] - self.playerCoord[i]), self.moveSpeed)
			newCoord.append(self.playerCoord[i])
			if(newCell.GetCenter()[i] > self.playerCoord[i]):
				newCoord[i] += moveLen
			else:
				newCoord[i] -= moveLen
		self.playerCoord = tuple(newCoord)

	def ChangeDirection(self, newDirection):
		if self.isMoving or newDirection > 3 or newDirection < 0:
			return
		if self.moveDirection != newDirection:
			self.moveDirection = newDirection
			self.curFrame = 0
			self.numFrame = len(self.playerFrame[self.moveDirection])

		if self.playerCell.GetAdj(self.moveDirection) != None:
			self.isMoving = True

	def ChangeCell(self, newCellIndex):
		for direction in range(4):
			adjCell = self.playerCell.GetAdj(direction)
			if adjCell != None and adjCell.GetCellIndex() == newCellIndex:
				self.ChangeDirection(direction)
				return

	def HandleEvent(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_UP]:
			self.ChangeDirection(0)
		if key[pygame.K_DOWN]:
			self.ChangeDirection(2)
		if key[pygame.K_LEFT]:
			self.ChangeDirection(3)
		if key[pygame.K_RIGHT]:
			self.ChangeDirection(1)

	def HandleEventFromFile(self):
		if self.isMoving:
			return
		key = pygame.key.get_pressed()
		if key[pygame.K_RETURN]:
			direction = self.instructionFile.read(1)
			if direction == '':
				return
			self.ChangeDirection(int(direction))