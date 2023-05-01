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
		self.backgroundImage = {
			"Obstacle": pygame.transform.scale(Const.CELL_IMAGE_LIST[1], (cellLen, cellLen))
		}

	def DisplayBackgroundImage(self):
		self.gameScreen.blit(self.backgroundImage["Obstacle"], self.cellCoord)

class EmptyCell(Cell):
	def __init__(self, gameScreen, cellCoord, cellIndex, cellLen):
		Cell.__init__(self, cellCoord, cellIndex, cellLen)

		self.gameScreen = gameScreen
		self.cellColor = "Null"
		self.backgroundImage = {
			"Empty Null": pygame.transform.scale(Const.CELL_IMAGE_LIST[0], (cellLen, cellLen)),
			"Empty Red": pygame.transform.scale(Const.CELL_IMAGE_LIST[1], (cellLen, cellLen)),
			"Empty Blue": pygame.transform.scale(Const.CELL_IMAGE_LIST[2], (cellLen, cellLen)),
			"Empty Green": pygame.transform.scale(Const.CELL_IMAGE_LIST[3], (cellLen, cellLen)),
			"Empty Yellow": pygame.transform.scale(Const.CELL_IMAGE_LIST[4], (cellLen, cellLen))
		}

	def DisplayBackgroundImage(self):
		self.gameScreen.blit(self.backgroundImage["Empty " + self.cellColor], self.cellCoord)

	def ChangeCellColor(self, newColor):
		self.cellColor = newColor


class DestroyableCell(EmptyCell):
	def __init__(self, gameScreen, cellCoord, cellIndex, cellLen):
		EmptyCell.__init__(self, gameScreen, cellCoord, cellIndex, cellLen)

		self.isDestroyed = False
		self.backgroundImage["Obstacle"] = pygame.transform.scale(Const.CELL_IMAGE_LIST[0], (cellLen, cellLen))

	def DisplayBackgroundImage(self):
		if self.isDestroyed == False:
			self.gameScreen.blit(self.backgroundImage["Obstacle"], self.cellCoord)
		else:
			EmptyCell.DisplayBackgroundImage(self)

	def DestroyCell(self):
		self.isDestroyed = True



