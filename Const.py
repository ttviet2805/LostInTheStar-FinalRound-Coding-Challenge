import pygame

CELL_LENGTH = 100
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/Cell/tile_{i}.png') for i in range(0, 3)]
PLAYER_FRAME_DICT = {
	"Down": [pygame.image.load(f'Assets/Images/Player/Down{i}.png') for i in range(0, 6)],
	"Up": [pygame.image.load(f'Assets/Images/Player/Up{i}.png') for i in range(0, 6)],
	"Left": [pygame.image.load(f'Assets/Images/Player/Left{i}.png') for i in range(0, 6)],
	"Right": [pygame.image.load(f'Assets/Images/Player/Right{i}.png') for i in range(0, 6)]
}