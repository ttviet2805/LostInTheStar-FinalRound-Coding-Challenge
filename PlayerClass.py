import pygame
import Const
import CellClass
import PortalClass
import PlayerStatus

class Player():
	def __init__(self, gameScreen, ID, playerName, statusInfo, curCell):
		# Status
		self.playerID = ID
		self.isAlive = True
		self.playerName = playerName
		print(playerName)
		self.status = PlayerStatus.PlayerStatus(gameScreen, ID, self.isAlive, playerName, Const.PLAYER_COLOR[ID], statusInfo[0][ID], statusInfo[1])

		self.gameScreen = gameScreen
		self.playerCell = curCell
		self.playerCell.AddPlayer(self.playerID)
		self.playerCoord = (-1, -1)
		self.playerFrameHeight = self.playerCell.GetLen() / 6 * 7
		self.playerFrameWidth = self.playerFrameHeight / 7 * 5
		# self.playerPadding = ((self.playerCell.GetLen() - self.playerFrameWidth) / 2, (self.playerCell.GetLen() - self.playerFrameHeight) * 2) 
		self.playerPadding = ((self.playerCell.GetLen() - self.playerFrameWidth) / 2 + self.playerCell.GetLen() / 15, (- self.playerFrameHeight) / 2) 

		self.playerFrame = []
		for listFrame in Const.PLAYER_FRAME_LIST:
			playerFrameList = []
			step = len(listFrame) // 4
			for i in range(self.playerID * step, self.playerID * step + step):
				frame = listFrame[i]
				playerFrameList.append(pygame.transform.scale(frame, (self.playerFrameWidth, self.playerFrameHeight)))
			self.playerFrame.append(playerFrameList)

		self.moveDirection = 2
		self.animationDirection = 0
		self.curFrame = 0
		self.numFrame = len(self.playerFrame[self.animationDirection])
		self.isMoving = False
		self.moveSpeed = 15

		self.playerPortal = PortalClass.Portal(gameScreen, curCell)
		self.appearFrame = 9

	def GetInfo(self):
		return self.status.GetInfo()

	def UpdateCoord(self):
		if self.playerCoord == (-1, -1):
			self.playerCoord = self.playerCell.GetPlayerPos(self.playerID)

	def DisplayFrame(self):
		self.gameScreen.blit(self.playerFrame[self.animationDirection][self.curFrame], (self.playerCoord[0] + self.playerPadding[0], self.playerCoord[1] + self.playerPadding[1]))

	def GetIsMoving(self):
		return self.isMoving or self.appearFrame > 0

	def GetID(self):
		return self.playerID

	def GetIsAlive(self):
		return self.isAlive

	def MoveFrame(self):
		if(self.appearFrame > 0):
			pygame.mixer.Sound.play(Const.PLAYER_APPEAR_SOUND)
			self.playerPortal.MoveFrame()
			self.appearFrame -= 1
			return
		if self.isMoving:
			self.MovePlayer()
		self.DisplayFrame()
		self.curFrame = (self.curFrame + 1) % self.numFrame

	def MovePlayer(self):
		newCell = self.playerCell.GetAdj(self.moveDirection)
		if self.playerCoord == newCell.GetPlayerPos(self.playerID):
			self.playerCell = newCell
			self.playerCoord = self.playerCell.GetPlayerPos(self.playerID)
			self.isMoving = False
			return
		newCoord = []
		for i in range(0, 2):
			moveLen = min(abs(newCell.GetPlayerPos(self.playerID)[i] - self.playerCoord[i]), self.moveSpeed)
			newCoord.append(self.playerCoord[i])
			if(newCell.GetPlayerPos(self.playerID)[i] > self.playerCoord[i]):
				newCoord[i] += moveLen
			else:
				newCoord[i] -= moveLen
		self.playerCoord = tuple(newCoord)

	def ChangeAnimation(self, newAnimation):
		if self.animationDirection != newAnimation:
			self.animationDirection = newAnimation
			self.curFrame = 0
			self.numFrame = len(self.playerFrame[self.animationDirection])

	def ChangeDirection(self, newDirection):
		if self.isMoving or newDirection > 3 or newDirection < 0:
			return
		if self.moveDirection != newDirection:
			self.moveDirection = newDirection
		if newDirection == 1 or newDirection == 3:
			self.ChangeAnimation(newDirection // 2)

		if self.playerCell.GetAdj(self.moveDirection) != None and self.isMoving == False:
			self.playerCell.RemovePlayer(self.playerID)
			self.playerCell.GetAdj(self.moveDirection).AddPlayer(self.playerID)
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

	def drawStatus(self):
		self.status.displayStatusImage()

	def updateScore(self, curScore):
		self.status.updateScore(curScore)

	def updateAlive(self, isAlive):
		if self.isAlive == True and isAlive == False:
			pygame.mixer.Sound.play(Const.PLAYER_DIE_SOUND)
			self.ChangeAnimation(2)
		self.isAlive = isAlive
		self.status.updateAlive(isAlive)