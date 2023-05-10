import pygame
import Const
import ButtonClass
import InGame

class Menu():
	def __init__(self):
		# pygame.init()

		# Menu Screen
		self.gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()
		pygame.display.flip()
		pygame.display.set_caption("Lost In The Star")

		# Menu Background
		self.backgroundImage = pygame.transform.scale(Const.MENU_BACKGROUND, (self.screenWidth, self.screenHeight))

		print(self.screenWidth, self.screenHeight)

		# Run
		self.running = True
		self.clock = pygame.time.Clock()

		# Load Lost Star Image
		self.lostStarSize = (self.screenWidth * 3 / 10, self.screenHeight * 4 / 10)
		self.lostStarImage = pygame.transform.scale(Const.LOST_STAR_IMAGE, self.lostStarSize)
		self.lostStarCoord = ((self.screenWidth / 2 - self.lostStarSize[0]) / 2, (self.screenHeight - self.lostStarSize[1]) / 2)

		# Load Start Image
		self.startButtonSize = (self.screenWidth * 1.5 / 10, self.screenHeight * 1.5 / 10)
		self.startButtonImage = pygame.transform.scale(Const.START_BUTTON_IMAGE, self.startButtonSize)
		self.startButtonCoord = (self.screenWidth / 2 + (self.screenWidth / 2 - self.startButtonSize[0]) / 2, self.screenHeight * 3 / 4 + (self.screenHeight * 1 / 4 - self.startButtonSize[1]) / 2)
		self.startButton = ButtonClass.Button(self.startButtonImage, self.startButtonCoord)


	def Run(self):
		while self.running:
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_presses = pygame.mouse.get_pressed()
				
			self.gameScreen.blit(self.backgroundImage, (0, 0))
			self.gameScreen.blit(self.lostStarImage, self.lostStarCoord)

			self.startButton.draw(self.gameScreen)

			cur = self.startButton.isClicked(self.gameScreen)
			if cur == True:
				self.running = False
				InGame.Run()


			pygame.display.update()

