import pygame
import Const
import CellClass

import json

def getMap(step):
	mapFile = open("Assets/Example.json")

	curMap = []

	mapData = json.load(mapFile)

	curList = mapData[str(step)]['map']['grid']

	m = mapData[str(step)]['map']['rows']
	n = mapData[str(step)]['map']['columns']

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
		self.mapList = getMap(1)[2]
		self.M = getMap(1)[0]
		self.N = getMap(1)[1]

		# Map Image
		self.mapSize = mapSize
		self.mapImage = []

		cellLen = self.mapSize // self.N
		mapInitCoord += (self.mapSize - cellLen * self.N) / 2

		# Create List Cell in Map
		for i in range(0, self.M):
			mapImageRow = []
			for j in range(0, self.N):
				if self.mapList[i][j] == '0' or self.mapList[i][j] == '.':
					mapImageRow.append(CellClass.EmptyCell(self.gameScreen, (j * cellLen + mapInitCoord, i * cellLen), cellLen))
				else:
					mapImageRow.append(CellClass.ObstacleCell(self.gameScreen, (j * cellLen + mapInitCoord, i * cellLen), cellLen))
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

	def GetCell(self, row, col):
		return self.mapImage[row % self.N][col % self.N]