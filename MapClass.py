import pygame
import Const
import CellClass

class Map():
	def __init__(self, gameScreen, mapList, mapSize, mapInitCoord):
		self.gameScreen = gameScreen
		self.mapList = mapList
		self.mapSize = mapSize
		self.N = len(self.mapList)
		self.mapImage = []

		cellLen = self.mapSize // self.N
		mapInitCoord += (self.mapSize - cellLen * self.N) / 2

		# create map
		for i in range(0, self.N):
			mapImageRow = []
			for j in range(0, self.N):
				if self.mapList[i][j] == '0' or self.mapList[i][j] == '.':
					mapImageRow.append(CellClass.EmptyCell(self.gameScreen, (j * cellLen + mapInitCoord, i * cellLen), cellLen))
				else:
					mapImageRow.append(CellClass.ObstacleCell(self.gameScreen, (j * cellLen + mapInitCoord, i * cellLen), cellLen))
			self.mapImage.append(mapImageRow)
		
		# create graph
		for i in range(0, self.N):
			for j in range(0, self.N):
				for dir in range(0, 4):
					ni = i + Const.CELL_MOVE[dir][0]
					nj = j + Const.CELL_MOVE[dir][1]
					if ni < 0 or ni >= self.N or nj < 0 or nj >= self.N or isinstance(self.mapImage[ni][nj], CellClass.ObstacleCell):
						continue
					self.mapImage[i][j].AddAdj(self.mapImage[ni][nj], dir)

	def DisplayMap(self):
		for mapImageRow in self.mapImage:
			for cell in mapImageRow:
				cell.DisplayBackgroundImage()

	def GetCell(self, row, col):
		return self.mapImage[row % self.N][col % self.N]