import pygame
import Const

class Cell():
	def __init__(self, cellCoord, cellIndex, cellLen):
		self.cellLen = cellLen
		self.cellCoord = cellCoord
		self.cellIndex = cellIndex
		self.listAdj = [None, None, None, None]

	def AddAdj(self, adjCell, pos):
		if pos < 0 or pos > 3:
			return
		self.listAdj[pos] = adjCell

	def GetCellIndex(self):
		return self.cellIndex

	def GetCenter(self):
		return self.cellCoord

	def GetAdj(self, pos):
		if pos < 0 or pos > 3:
			return None
		return self.listAdj[pos]

	def GetLen(self):
		return self.cellLen

class ObstacleCell(Cell):
	def __init__(self, gameScreen, cellCoord, cellIndex, cellLen):
		Cell.__init__(self, cellCoord, cellIndex, cellLen)

		self.gameScreen = gameScreen
		self.backgroundImage = [
			pygame.transform.scale(Const.CELL_IMAGE_LIST[10], (cellLen, cellLen))
		]

	def DisplayBackgroundImage(self):
		self.gameScreen.blit(self.backgroundImage[0], self.cellCoord)

class EmptyCell(Cell):
	def __init__(self, gameScreen, cellCoord, cellIndex, cellLen, cellColor):
		Cell.__init__(self, cellCoord, cellIndex, cellLen)

		self.gameScreen = gameScreen
		self.cellColor = cellColor
		self.isLocked = False
		self.backgroundImage = [
			pygame.transform.scale(Const.CELL_IMAGE_LIST[i], (cellLen, cellLen)) for i in range(10)
		]

	def DisplayBackgroundImage(self):
		self.gameScreen.blit(self.backgroundImage[self.cellColor], self.cellCoord)
		# if self.isLocked:
		# 	self.gameScreen.blit(self.backgroundImage[5], self.cellCoord)

	def ChangeCellColor(self, newColor):
		self.cellColor = newColor

	def LockCell(self):
		self.cellColor = 5