import pygame
import Const

class Cell():
	def __init__(self, cellCoord):
		self.cellLength = Const.CELLLENGTH
		self.cellCoord = cellCoord

class ObstacleCell(Cell):
	def __init__(self, gameScreen, cellCoord):
		Cell.__init__(self, cellCoord)

		self.gameScreen = gameScreen
		self.backgroundImage = {
			"Obstacle": pygame.image.load(f'Assets/Images/Cell/tile_0.png')
		}

	def DisplayBackgroundImage(self):
		self.gameScreen.blit(self.backgroundImage["Obstacle"], self.cellCoord)

class EmptyCell(Cell):
	def __init__(self, gameScreen, cellCoord):
		Cell.__init__(self, cellCoord)

		self.gameScreen = gameScreen
		self.cellColor = "Null"
		self.backgroundImage = {
			"Empty Null": pygame.image.load(f'Assets/Images/Cell/tile_2.png'),
			"Empty Red": pygame.image.load(f'Assets/Images/Cell/tile_0.png'),
			"Empty Blue": pygame.image.load(f'Assets/Images/Cell/tile_0.png'),
			"Empty Green": pygame.image.load(f'Assets/Images/Cell/tile_0.png'),
			"Empty Yellow": pygame.image.load(f'Assets/Images/Cell/tile_0.png')
		}

	def DisplayBackgroundImage(self):
		self.gameScreen.blit(self.backgroundImage["Empty " + self.cellColor], self.cellCoord)

	def ChangeCellColor(self, newColor):
		self.cellColor = newColor


class DestroyableCell(EmptyCell):
	def __init__(self, gameScreen, cellCoord):
		EmptyCell.__init__(self, gameScreen, cellCoord)

		self.isDestroyed = False
		self.backgroundImage["Obstacle"] = pygame.image.load(f'Assets/Images/Cell/tile_1.png')

	def DisplayBackgroundImage(self):
		if self.isDestroyed == False:
			self.gameScreen.blit(self.backgroundImage["Obstacle"], self.cellCoord)
		else:
			EmptyCell.DisplayBackgroundImage(self)

	def DestroyCell(self):
		self.isDestroyed = True



