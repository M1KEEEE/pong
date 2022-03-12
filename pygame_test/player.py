import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((25, 150))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.center = (25, 300)
