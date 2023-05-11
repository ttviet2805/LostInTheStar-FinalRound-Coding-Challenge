import pygame
import json

MSI = (1536, 864)

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

GAME_BACKGROUND = pygame.image.load('Assets/Images/Background/Game-Background.png')
GAME_BACKGROUND_ENGINE = [
	[pygame.image.load(f'Assets/Images/Background/left-engine-anim-{i}.png') for i in range(4)],
	[pygame.image.load(f'Assets/Images/Background/right-engine-anim-{i}.png') for i in range(4)]
]

PLAYER_AVA = [pygame.image.load(f'Assets/Images/Status/Avatar_{i}.png') for i in range(1, 5)]
PLAYER_AVA_DEAD = [pygame.image.load(f'Assets/Images/Status/deadAvatar_{i}.png') for i in range(1, 5)]

CELL_LENGTH = 100
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/Cell/tile_{i}.png') for i in range(12)]
CELL_MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
PLAYER_FRAME_LIST = [
	[pygame.image.load(f'Assets/Images/Player/player{i}-left-{j}.png') for i in range(1, 5) for j in range(12)],
	[pygame.image.load(f'Assets/Images/Player/player{i}-right-{j}.png') for i in range(1, 5) for j in range(12)],
	[pygame.image.load(f'Assets/Images/Player/player{i}-ghost-{j}.png') for i in range(1, 5) for j in range(4)]
]
PORTAL_FRAME_LIST = [pygame.image.load(f'Assets/Images/Portal/portal-{i}.png') for i in range(9)]

# Status
STATUS_BACKGROUND = pygame.image.load('Assets/Images/Status/Status.png')
PLAYER_IMAGE = [
	pygame.image.load(f'Assets/Images/Player/ava{i}.png') for i in range(4)
]

# Map file
mapFile = open("Assets/Example.json")
mapData = json.load(mapFile)
MAP_NORM = '.'
MAP_OBS = '#'
MAP_OZ = '#'

# Leaderboard
LEADERBOARD_BG = pygame.image.load("Assets/Images/Background/Leaderboard-Background.png")
RANK_CUP = [
	pygame.image.load(f'Assets/Images/Leaderboard/rank{i}.png') for i in range(1, 5)
]
BACK_BUTTON_IMAGE = pygame.image.load('Assets/Images/Leaderboard/back-button.png')

# Menu
MENU_BACKGROUND = pygame.image.load('Assets/Images/Background/Menu-Background.png')
LOST_STAR_IMAGE = pygame.image.load('Assets/Images/Menu/title.png')
START_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/start-button.png')
TWO_PLAYER_IMAGE = pygame.image.load('Assets/Images/Menu/2player-button.png')
FOUR_PLAYER_IMAGE = pygame.image.load('Assets/Images/Menu/4player-button.png')
CHOOSE_IMAGE = pygame.image.load('Assets/Images/Menu/choose.png')
TICK_IMAGE = [
	pygame.image.load('Assets/Images/Menu/checkbox-unchecked.png'),
	pygame.image.load('Assets/Images/Menu/checkbox-checked.png')
]
MAP_SIZE_IMAGE = pygame.image.load('Assets/Images/Menu/dropdown.png')
UP_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/up.png')
DOWN_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/down.png')




