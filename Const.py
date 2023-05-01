import pygame
import json

CELL_LENGTH = 100
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/Cell/tile_{i}.png') for i in range(0, 8)]
CELL_MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
PLAYER_FRAME_LIST = [
	[pygame.image.load(f'Assets/Images/Player/Up{i}.png') for i in range(0, 6)],
	[pygame.image.load(f'Assets/Images/Player/Right{i}.png') for i in range(0, 6)],
	[pygame.image.load(f'Assets/Images/Player/Down{i}.png') for i in range(0, 6)],
	[pygame.image.load(f'Assets/Images/Player/Left{i}.png') for i in range(0, 6)]
]

# Status
STATUS_BACKGROUND = pygame.image.load('Assets/Images/Status/Status.png')
PLAYER_IMAGE = pygame.image.load('Assets/Images/Status/Songoku.png')

# Map file
mapFile = open("Assets/Example.json")
mapData = json.load(mapFile)