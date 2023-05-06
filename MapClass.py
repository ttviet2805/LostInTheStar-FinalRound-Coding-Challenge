import pygame
import Const
import CellClass

def getMap(step):
	curMap = []

	curList = Const.mapData[str(step)]['map']['grid']

	m = Const.mapData[str(step)]['map']['rows']
	n = Const.mapData[str(step)]['map']['columns']

	for i in curList:
		row = []
		for j in i:
			row.append(j)
		curMap.append(row)

	return (m, n, curMap)

class Map():
	def __init__(self, gameScreen, mapSize, mapInitCoord):
		self.gameScreen = gameScreen

		# Map List
		self.M, self.N, self.mapList = getMap(0)

		# Map Image
		self.mapSize = mapSize
		self.mapImage = []

		self.cellLen = self.mapSize // self.N
		self.mapInitCoord = mapInitCoord + (self.mapSize - self.cellLen * self.N) / 2

		# Create List Cell in Map
		for i in range(0, self.M):
			mapImageRow = []
			for j in range(0, self.N):
				if self.mapList[i][j] == '.':
					mapImageRow.append(CellClass.EmptyCell(self.gameScreen, (j * self.cellLen + self.mapInitCoord, i * self.cellLen), (i, j), self.cellLen, 0))
				else:
					mapImageRow.append(CellClass.ObstacleCell(self.gameScreen, (j * self.cellLen + self.mapInitCoord, i * self.cellLen), (i, j), self.cellLen))
			self.mapImage.append(mapImageRow)
		
		# Create Graph
		for i in range(0, self.M):
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

	def UpdateMap(self, step):
		newMapList = getMap(step)[2]

		for i in range(self.M):
			for j in range(self.N):
				if newMapList[i][j] != self.mapList[i][j]:
					if newMapList[i][j] == '#':
						self.mapImage[i][j].LockCell()
					elif newMapList[i][j].isupper():
						newColor = 0
						if newMapList[i][j] == "A":
							newColor = 1
						elif newMapList[i][j] == "B":
							newColor = 2
						elif newMapList[i][j] == "C":
							newColor = 3
						elif newMapList[i][j] == "D":
							newColor = 4
						self.mapImage[i][j] = CellClass.EmptyCell(self.gameScreen, (j * self.cellLen + self.mapInitCoord, i * self.cellLen), (i, j), self.cellLen, newColor)
					else:
						newColor = 0
						if newMapList[i][j] == "a":
							newColor = 1
						elif newMapList[i][j] == "b":
							newColor = 2
						elif newMapList[i][j] == "c":
							newColor = 3
						elif newMapList[i][j] == "d":
							newColor = 4
						self.mapImage[i][j] = CellClass.EmptyCell(self.gameScreen, (j * self.cellLen + self.mapInitCoord, i * self.cellLen), (i, j), self.cellLen, newColor)
						self.mapImage[i][j].LockCell()
		self.mapList = newMapList

	def GetCell(self, row, col):
		return self.mapImage[row % self.N][col % self.N]

	def getScore(self, ID):
		X = 0
		Y = 0
		
		if ID == 0:
			X, Y = 'a', 'A'
		if ID == 1:
			X, Y = 'b', 'B'
		if ID == 2:
			X, Y = 'c', 'C'
		if ID == 3:
			X, Y = 'd', 'D'

		curScore = 0

		for i in range(self.M):
			for j in range(self.N):
				if self.mapList[i][j] == X or self.mapList[i][j] == Y:
					curScore += 1

		return curScore