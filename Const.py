import pygame
import json

# Player
PLAYER_COLOR = ["RED", "GREEN", "BLUE", "YELLOW"]
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (146, 146, 146)
WHITE = (255, 255, 255)
SNOW = (255, 250, 250)
BLACK = (0, 0, 0)
PLAYER_COLOR_DICT = {
	"RED": (255, 0, 0),
	"GREEN": (0, 255, 0),
	"BLUE": (0, 0, 255),
	"YELLOW": (255, 255, 0)
}
MAP_COLOR = (127, 115, 82)
BACKGROUND_COLOR = (92, 98, 108)




CELL_LENGTH = 100
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/Cell/tile_{i}.png') for i in range(11)]
CELL_MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
PLAYER_FRAME_LIST = [
	[pygame.image.load(f'Assets/Images/Player/Up{i}.png') for i in range(6)],
	[pygame.image.load(f'Assets/Images/Player/Right{i}.png') for i in range(6)],
	[pygame.image.load(f'Assets/Images/Player/Down{i}.png') for i in range(6)],
	[pygame.image.load(f'Assets/Images/Player/Left{i}.png') for i in range(6)]
]
PORTAL_FRAME_LIST = [pygame.image.load(f'Assets/Images/Portal/portal-{i}.png') for i in range(9)]

# Status
STATUS_BACKGROUND = pygame.image.load('Assets/Images/Status/Status.png')
PLAYER_IMAGE = pygame.image.load('Assets/Images/Status/Songoku.png')

# Map file
mapFile = open("Assets/Example.json")
mapData = json.load(mapFile)